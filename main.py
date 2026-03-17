from flask import Flask, request, jsonify, render_template
from google import genai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"reply": "No JSON received"})

        user_message = data.get("message")

        if not user_message:
            return jsonify({"reply": "No message provided"})

        response = client.models.generate_content(
           model="gemini-2.0-flash", contents=user_message
        )

        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({"reply": f"ERROR: {str(e)}"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
