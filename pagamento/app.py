from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

AUTH_SERVICE_URL = 'http://localhost:5000/validate'

def validate_token(token):
    response = requests.post(AUTH_SERVICE_URL, headers={'Authorization': f'Bearer {token}'})
    return response.json()

@app.route('/process', methods=['POST'])
def process_payment():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Authorization token is missing'}), 401

    validation_response = validate_token(token)
    if validation_response.get('status') != 'valid':
        return jsonify({'error': 'Invalid token'}), 401

    data = request.json
    amount = data.get('amount')
    if amount:
        return jsonify({'status': 'Payment processed', 'amount': amount})
    else:
        return jsonify({'error': 'Invalid payment data'}), 400

if __name__ == '__main__':
    app.run(port=5001)
