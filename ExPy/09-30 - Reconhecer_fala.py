import openai
import pyttsx3

# Configure a sua chave de API do OpenAI
openai.api_key = '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'

def ask_question(question):
    # Chama a API do OpenAI para obter a resposta à pergunta
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extrai a resposta gerada pelo modelo
    answer = response.choices[0].text.strip()

    return answer

def speak(text):
    # Inicializa o mecanismo de síntese de fala
    engine = pyttsx3.init()

    # Define a voz utilizada para a síntese de fala
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Reproduz o texto em voz alta
    engine.say(text)
    engine.runAndWait()

# Solicita que o usuário digite a pergunta
question = input("Faça uma pergunta: ")

# Chama a função para obter a resposta do chatbot
answer = ask_question(question)

# Reproduz a resposta em voz alta
speak(answer)