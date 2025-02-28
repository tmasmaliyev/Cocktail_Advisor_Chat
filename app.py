from flask import Flask, request, jsonify
from ai_functionalities import chatbot_response

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    text = data.get("text", "")
    
    return jsonify({"result": chatbot_response(text)})

if __name__ == '__main__':
    app.run(debug=True, port=5000) 