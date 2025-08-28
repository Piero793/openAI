from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

chat_history = [
    {"role": "system", "content": "Sei un assistente cordiale e disponibile."}
]

def chat_with_openai():
    while True:
        user_input = input("Tu: ")
        
        if user_input.lower() == "stop":
            print("Chat terminata.")
            break
        
        chat_history.append({"role": "user", "content": user_input})

        try:
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=chat_history,
                stream=True
            )
            
            print("AI: ", end="", flush=True)
            assistant_response = ""
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    part = chunk.choices[0].delta.content
                    print(part, end="", flush=True)
                    assistant_response += part
            print()

            chat_history.append({"role": "assistant", "content": assistant_response})

        except Exception as e:
            print(f"Si è verificato un errore: {e}")

chat_with_openai()