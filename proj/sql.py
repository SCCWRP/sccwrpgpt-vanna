from .utils.vanna import vn
from .utils.cache import cache, requires_cache
from flask import Blueprint, jsonify, Response, request, redirect, url_for

sql_bp = Blueprint('sql_bp', __name__)

@sql_bp.route('/api/v0/generate_sql', methods=['GET'])
def generate_sql():
    question = request.args.get('question')

    if question is None:
        return jsonify({"type": "error", "error": "No question provided"})

    id_ = cache.generate_id(question=question)
    sql = vn.generate_sql(question=question)

    cache.set(id=id_, field='question', value=question)
    cache.set(id=id_, field='sql', value=sql)

    return jsonify(
        {
            "type": "sql", 
            "id": id_,
            "text": sql,
        })

@sql_bp.route('/api/v0/run_sql', methods=['GET'])
@requires_cache(['sql'])
def run_sql(id: str, sql: str):
    try:
        df = vn.run_sql(sql=sql)

        cache.set(id=id, field='df', value=df)

        return jsonify(
            {
                "type": "df", 
                "id": id,
                "df": df.head(10).to_json(orient='records'),
            })

    except Exception as e:
        return jsonify({"type": "error", "error": str(e)})
