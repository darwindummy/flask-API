from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Render!"})

@app.route('/process', methods=['POST'])
def process_payload():
    data = request.get_json()
    number1 = data.get("number1", 0)
    number2 = data.get("number2", 0)
    result = number1 + number2
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
