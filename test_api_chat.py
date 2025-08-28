from openai import OpenAI

client = OpenAI(api_key="qui inserirai la tua chiave API di openAI")
chat_history = []

def chat_with_openai():
    chat_history.append({"role": "system", "content": "Usa un tono cordiale"})

    while True:
        user_input = input("Tu:")
        chat_history.append({"role": "user", "content": user_input})
        if user_input.lower() == "stop":
            break   

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",  #consultare la documentazione di openAI per ulteriori dettagli sul modello da utilizzare
    messages=chat_history,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta is not None:
        print(chunk.choices[0].delta.content, end="")
