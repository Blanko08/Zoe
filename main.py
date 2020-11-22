import time
import datetime
import pyttsx3
import speech_recognition as sr
import requests
import pyaudio

#Esta función hace hablar a Zoe
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('voice', 'spanish')
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()

#Aquí recogeremos el audio del usuario
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    said = ""
    try:
        said = r.recognize_google(audio, language='es-ES')
        print("Has dicho: " + said)
    except:
        print("Error al recoger audio")
    return said.lower()


#Aquí creamos una función para "despertar" a Zoe
def despertar(text):
    ready = ['ey zoe', 'hey zoe', 'ok zoe', 'oye zoe'] #Lista de palabras que van a despertar a Zoe

    text = text.lower()

    for phrase in ready:
        if phrase in text:
            return True

    #Devuelve Falso si no encuentra la palabra que hace despertar a Zoe
    return False


#Función de saludo al iniciar el programa
def saludo():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Buenos días!")
    elif hour >= 12 and hour < 21:
        speak("Buenas tardes!")
    else:
        speak("Buenas noches!")


def clima():
    api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=4369b55a0d2b99d0dfabd006ca894f40&units=metric&lang=es&q='
    speak("Dime el nombre de la ciudad")
    city = get_audio()
    print(city)

    url = api_address + city
    respuesta = requests.get(url)
    clima = respuesta.json()

    datos_clima = clima['weather'][0]['description'] + ". La temperatura actualmente es de" + str(clima['main']['temp']) + "grados"

    speak(datos_clima)


while True:
    print("Escuchando...")
    text = get_audio().lower()

    if despertar(text) == True:
        saludo()
        speak("¿En qué puedo ayudarte?")
        print("Escuchando...")
        text = get_audio()

        if 'hola' in text:
            speak("¿Hola, como estás?")
        elif 'como te llamas' or 'cual es tu nombre' in text:
            speak("Me llamo Zoe")
        elif 'tiempo' or 'clima' in text:
            clima()
        elif 'apagate' in text:
            speak("Hasta luego")
            break
