from .utils.vanna import vn
from .utils.cache import cache, requires_cache
from flask import Blueprint, jsonify

questions_bp = Blueprint('questions_bp', __name__)


@questions_bp.route('/api/v0/generate_questions', methods=['GET'])
def generate_questions():
    return jsonify({
        "type": "question_list", 
        "questions": vn.generate_questions(),
        "header": "Here are some questions you can ask:"
        })

@questions_bp.route('/api/v0/generate_followup_questions', methods=['GET'])
@requires_cache(['df', 'question'])
def generate_followup_questions(id: str, df, question):
    followup_questions = vn.generate_followup_questions(question=question, df=df)

    cache.set(id=id, field='followup_questions', value=followup_questions)

    return jsonify(
        {
            "type": "question_list", 
            "id": id,
            "questions": followup_questions,
            "header": "Here are some followup questions you can ask:"
        })

@questions_bp.route('/api/v0/load_question', methods=['GET'])
@requires_cache(['question', 'sql', 'df', 'fig_json', 'followup_questions'])
def load_question(id: str, question, sql, df, fig_json, followup_questions):
    try:
        return jsonify(
            {
                "type": "question_cache", 
                "id": id,
                "question": question,
                "sql": sql,
                "df": df.head(10).to_json(orient='records'),
                "fig": fig_json,
                "followup_questions": followup_questions,
            })

    except Exception as e:
        return jsonify({"type": "error", "error": str(e)})

@questions_bp.route('/api/v0/get_question_history', methods=['GET'])
def get_question_history():
    return jsonify({"type": "question_history", "questions": cache.get_all(field_list=['question']) })