from flask import Flask, render_template, request, jsonify, abort
from errors.http_errors import bad_request
from find_info import find_info
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/summary", methods=["POST"])
def process():
    search = request.get_json().get("search")
    if(search is None):
        return bad_request("Search parameter is required")
    result, img_url = find_info(search)
    return jsonify({
        "summary": result.summary,
        "facts": result.facts,
        "topics_of_interest": result.topics_of_interest,
        "ice_breakers": result.ice_breakers,
        "img_url": img_url
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4567, debug=True)

