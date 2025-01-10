from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Load OpenAI API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat_with_ai(messages, model="gpt-4o-mini", max_tokens=100):
    """
    Engages in a conversation with the AI using the ChatCompletion interface.

    Parameters:
        messages (list): A list of messages to maintain the conversation context.
        model (str): The model to use (e.g., gpt-4o-mini).
        max_tokens (int): The maximum number of tokens to generate.

    Returns:
        str: The AI's response.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    # Initialize conversation context
    conversation = [{"role": "system", "content": "You are a helpful and witty assistant, that likes haikus every now and again."}]

    print("Chat with your AI! Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Add user input to conversation context
        conversation.append({"role": "user", "content": user_input})

        # Generate AI response
        ai_response = chat_with_ai(conversation)

        # Add AI response to conversation context
        conversation.append({"role": "assistant", "content": ai_response})

        # Print AI's response
        print(f"AI: {ai_response}")
