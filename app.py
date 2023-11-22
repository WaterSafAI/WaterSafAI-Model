from flask import Flask, request, jsonify
from prediction import predictor, mean_values

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict_endpoint():
    data = request.get_json()
    prediction = predictor.predict(data, mean_values)
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(debug=True)
