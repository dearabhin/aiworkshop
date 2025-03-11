import os
from google import genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("API_KEY")

# Initialize client
client = genai.Client(api_key=api_key)


@app.route('/home', methods=['GET'])
def home():
    return "Hell World"


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json  # Get input from request body
        if not data or "prompt" not in data:
            return jsonify({"error": "prompt not found in data"}), 400

        prompt = data["prompt"]
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt
        )

        return jsonify({"ai_response": response.text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)


