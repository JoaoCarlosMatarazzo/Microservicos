from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username == 'admin' and password == 'password':
        return jsonify({'token': 'secret-token'})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/validate', methods=['POST'])
def validate():
    token = request.headers.get('Authorization')
    if token == 'Bearer secret-token':
        return jsonify({'status': 'valid'})
    else:
        return jsonify({'status': 'invalid'}), 401

if __name__ == '__main__':
    app.run(port=5000)
