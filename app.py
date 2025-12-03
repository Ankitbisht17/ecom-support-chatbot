from flask import Flask, request, jsonify, render_template
from chatbot_core import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    # Renders templates/index.html
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    bot_reply = generate_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
