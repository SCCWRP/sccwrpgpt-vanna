from .utils.vanna import vn
from flask import Blueprint, request, jsonify

training_bp = Blueprint('training_bp', __name__)

@training_bp.route('/api/v0/get_training_data', methods=['GET'])
def get_training_data():
    df = vn.get_training_data()

    return jsonify(
    {
        "type": "df", 
        "id": "training_data",
        "df": df.head(25).to_json(orient='records'),
    })

@training_bp.route('/api/v0/remove_training_data', methods=['POST'])
def remove_training_data():
    # Get id from the JSON body
    id_ = request.json.get('id')

    if id_ is None:
        return jsonify({"type": "error", "error": "No id provided"})

    if vn.remove_training_data(id=id_):
        return jsonify({"success": True})
    else:
        return jsonify({"type": "error", "error": "Couldn't remove training data"})

@training_bp.route('/api/v0/train', methods=['POST'])
def add_training_data():
    question = request.json.get('question')
    sql = request.json.get('sql')
    ddl = request.json.get('ddl')
    documentation = request.json.get('documentation')

    try:
        id_ = vn.train(question=question, sql=sql, ddl=ddl, documentation=documentation)

        return jsonify({"id": id_})
    except Exception as e:
        print("TRAINING ERROR", e)
        return jsonify({"type": "error", "error": str(e)})