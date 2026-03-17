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
        user_message = request.json.get("message")

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=user_message
        )

        return jsonify({"reply": response.text})

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)