from flask import jsonify

def bad_request(message="Bad request"):
    return jsonify({
        "status": "Bad request",
        "status_code": 400,
        "message": message
    }), 400