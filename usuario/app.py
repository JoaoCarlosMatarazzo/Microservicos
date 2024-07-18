from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_payment():
    data = request.json
    amount = data.get('amount')
    if amount:
        return jsonify({'status': 'Payment processed', 'amount': amount})
    else:
        return jsonify({'error': 'Invalid payment data'}), 400

if __name__ == '__main__':
    app.run(port=5001)

