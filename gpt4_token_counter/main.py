from flask import Flask, request, jsonify
from token_counter import TokenCounter
from predict import count_string_tokens
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(
    app,
    resources={
        r"/count": {"origins": "chrome-extension://cabjhelnlpaelgbpmemiepfjpmiidpek"},
        r"/predict": {"origins": "chrome-extension://cabjhelnlpaelgbpmemiepfjpmiidpek"},
    },
)


@app.route("/count", methods=["POST", "OPTIONS"])
@cross_origin(
    origin="chrome-extension://cabjhelnlpaelgbpmemiepfjpmiidpek",
    headers=["Content-Type", "Authorization"],
)
def count():
    if request.method == "POST":
        # Handle POST request
        data = request.get_json()
        query = data.get("query", "")
        counter = TokenCounter(query)
        token_count = counter.count_tokens()
        return jsonify({"token_count": token_count})


@app.route("/predict", methods=["POST", "OPTIONS"])
@cross_origin(
    origin="chrome-extension://cabjhelnlpaelgbpmemiepfjpmiidpek",
    headers=["Content-Type", "Authorization"],
)
def predict():
    # Handle POST request
    data = request.get_json()
    text = data.get("text", "")
    model = data.get("model", "gpt-4")
    token_count = count_string_tokens(text, model)
    return jsonify({"token_count": token_count}), 200


if __name__ == "__main__":
    app.run(debug=True)
