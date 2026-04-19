import openai
import speech_recognition as sr
from gtts import gTTS
import os

openai.api_key = "SUA_API_KEY"

def ouvir_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse:", texto)
        return texto
    except:
        return ""

def responder_chatgpt(texto):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": texto}]
    )
    return resposta.choices[0].message.content

def falar(texto):
    tts = gTTS(texto, lang='pt')
    tts.save("resposta.mp3")
    os.system("start resposta.mp3")

texto = ouvir_audio()
resposta = responder_chatgpt(texto)
print("Resposta:", resposta)
falar(resposta)
