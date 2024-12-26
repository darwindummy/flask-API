import os
import requests
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
    # api_url = "https://fermyon.darwinbox.in/eventlistener/external?id=a67650c17a8f8f"
    api_url = "https://connectors.darwinbox.in/eventlistener/external?id=a676d45df8000e"
    logging.info("Incoming Json: %s",data)
    
    payloadJson = {
        data
    }
    logging.info("json Upload: %s", payloadJson)

    # Retrieve credentials from environment variables
    # api_username = os.getenv('API_USERNAME_priyansh')
    # api_password = os.getenv('API_PASSWORD_priyansh')
    api_username = os.getenv('API_USERNAME_priyansh_con')
    api_password = os.getenv('API_PASSWORD_priyansh_con')

    if not api_username or not api_password:
        return jsonify({"error": "API credentials not configured"}), 500

    try:
        # Call the API with Basic Auth
        response = requests.post(
            api_url,
            json=payloadJson,
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

@app.route('/deputy', methods=['GET'])
def openURL():
    # # Get incoming JSON payload
    # incoming_data = request.get_json()

    # # Log incoming payload
    # logging.info("Incoming JSON Payload: %s", incoming_data)

    # URL of the Deputy API
    api_url = "https://fermyon.darwinbox.in/eventlistener/external?id=a676d22ba24c61"

    # Retrieve credentials from environment variables
    api_username = os.getenv('API_USERNAME_vinitha')
    api_password = os.getenv('API_PASSWORD_vinitha')

    if not api_username or not api_password:
        logging.error("API credentials are not configured")
        return jsonify({"error": "API credentials not configured"}), 500

    # Collect headers and parameters
    incoming_headers = {key: value for key, value in request.headers.items()}
    incoming_params = request.args.to_dict()

    # Log incoming headers and parameters
    logging.info("Incoming Headers: %s", incoming_headers)
    logging.info("Incoming Query Parameters: %s", incoming_params)
    
    payloadJson = {
        "params" : incoming_params
    }

    try:
        # Call the Deputy API with Basic Auth
        response = requests.post(
            api_url,
            json=payloadJson,
            auth=(api_username, api_password)  # Basic Auth
        )

        # Log the Deputy API response
        logging.info("Deputy API Response Status Code: %s", response.status_code)
        logging.info("Deputy API Response Headers: %s", dict(response.headers))
        logging.info("Deputy API Response Text: %s", response.text)

        # Handle API response
        if response.status_code == 200:
            return (
                response.content,
                response.status_code,
                response.headers.items()
            )
        else:
            logging.error("Failed to call the Deputy API: %s", response.text)
            return jsonify({
                "status": "failure",
                "error": "Failed to call the Deputy API",
                "status_code": response.status_code,
                "response_text": response.text
            }), response.status_code
    except requests.exceptions.RequestException as e:
        logging.exception("An exception occurred while calling the Deputy API")
        return jsonify({
            "status": "failure",
            "error": f"An exception occurred: {str(e)}"
        }), 500
            
if __name__ == '__main__':
    app.run(debug=True)
