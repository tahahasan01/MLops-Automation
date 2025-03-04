from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the ML Prediction API! Use /predict to send data."

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.json["input"]
    result = predict(data)
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
