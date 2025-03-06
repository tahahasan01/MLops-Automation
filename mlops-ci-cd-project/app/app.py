from flask import Flask, request, jsonify
from model import predict  # Ensure the predict function is imported correctly

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the ML Prediction API! Use /predict to send data."

@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        # Get JSON data from the request
        data = request.json.get("input")
        
        # Validate if input data is provided
        if data is None:
            return jsonify({"error": "No input data provided"}), 400
        
        # Call the predict function from model.py
        result = predict(data)
        
        # Return the prediction as JSON
        return jsonify({"prediction": result})
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)