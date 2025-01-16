from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Chat history to maintain context
conversation = [{"role": "system", "content": "You are Earl, a helpful assistant."}]

@app.route("/")
def home():
    return render_template("index.html")  # Renders the frontend

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Add user input to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Generate response using the new API
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation,
            max_tokens=100,
            temperature=0.7
        )
        ai_response = response.choices[0].message.content.strip()

        # Add AI response to conversation
        conversation.append({"role": "assistant", "content": ai_response})

        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
