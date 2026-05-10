from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot.agent import initialize, ask

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data    = request.get_json()
    message = data.get('message', '').strip()

    if not message:
        return jsonify({'reply': 'Please type a message.'})

    reply = ask(message)
    return jsonify({'reply': reply})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    initialize()
    app.run(port=5000, debug=False)
