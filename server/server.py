from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)

# Route to get location names
@app.route('/get_name_names', methods=['GET'])
def get_name_names():
    response = jsonify({
        'name': util.get_name_names()
    })
    # Fix typo in header attribute and method
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Route to predict home price
@app.route('/predict_car_price', methods=['POST'])
def predict_car_price():
    try:
        # Safely parse input values
        engine_capacity = request.form["engine_capacity"]
        name = request.form['name']
        mileage = int(request.form['mileage'])
        year = int(request.form['year'])
        
        response = jsonify({
            'estimated_price': util.get_estimated_price(name,engine_capacity,mileage,year)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        # Return a proper error message in case of exceptions
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    print("Starting Python Flask Server for Car Price Prediction...")
    # Ensure artifacts are loaded before starting the server
    util.load_saved_artifacts()
    app.run(host="0.0.0.0", port=8000,debug=True)  # Enable debug mode for better error messages
