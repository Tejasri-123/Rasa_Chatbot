from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__, template_folder="templates")
CORS(app)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"  # Ensure Rasa is running on this URL

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@app.route("/send_message", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        print(f"User: {user_message}")  # Debugging

        response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})

        print(f"Rasa Response Status: {response.status_code}")  # Debugging

        if response.status_code == 200:
            rasa_response = response.json()
            print(f"Rasa Response: {rasa_response}")  # Debugging

            if rasa_response:
                full_response = " ".join([msg.get("text", "") for msg in rasa_response])  # Combine all text parts
                return jsonify({"bot_response": full_response})
            else:
                return jsonify({"bot_response": "No response from Rasa"}), 500
        else:
            return jsonify({"error": f"Failed to connect to Rasa: {response.status_code}"}), 500

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
