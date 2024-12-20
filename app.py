import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Vansh!"})

@app.route('/process', methods=['POST'])
def process_payload():
    # Get incoming data
    data = request.form.to_dict()

    # Use incoming data as payload for the next API
    payload = data

    # URL of the Validation API
    api_url = "https://integration3.qa.darwinbox.io/eventlistener/external?id=a676277581f82c"

    # Retrieve credentials from environment variables
    api_username = os.getenv('API_USERNAME')
    api_password = os.getenv('API_PASSWORD')

    if not api_username or not api_password:
        return jsonify({"error": "API credentials not configured"}), 500

    try:
        # Call the API with Basic Auth
        response = requests.post(
            api_url,
            json=payload,
            auth=(api_username, api_password)  # Basic Auth
        )

        # Handle API response
        if response.status_code == 200:
            return (response.content, response.status_code, response.headers.items())
        else:
            return jsonify({
                "status": "failure",
                "error": "Failed to call the Validation API",
                "status_code": response.status_code,
                "response_text": response.text
            }), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "failure",
            "error": f"An exception occurred: {str(e)}"
        }), 500

@app.route('/indeed',methods=['POST'])
def payload():
    data = request.get_json()
        # URL of the Validation API
    api_url = "https://fermyon.darwinbox.in/eventlistener/external?id=a67650c17a8f8f"

    # Retrieve credentials from environment variables
    api_username = os.getenv('API_USERNAME_priyansh')
    api_password = os.getenv('API_PASSWORD_priyansh')

    if not api_username or not api_password:
        return jsonify({"error": "API credentials not configured"}), 500

    try:
        # Call the API with Basic Auth
        response = requests.post(
            api_url,
            json=data,
            auth=(api_username, api_password)  # Basic Auth
        )

        # Handle API response
        if response.status_code == 200:
            return (response.content, response.status_code, response.headers.items())
        else:
            return jsonify({
                "status": "failure",
                "error": "Failed to call the Validation API",
                "status_code": response.status_code,
                "response_text": response.text
            }), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "failure",
            "error": f"An exception occurred: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
