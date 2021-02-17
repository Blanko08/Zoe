import datetime
import pyttsx3.drivers.sapi5
import speech_recognition as sr


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

#Función de saludo al iniciar el programa
def saludo():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Buenos días!")
    elif hour >= 12 and hour < 21:
        speak("Buenas tardes!")
    else:
        speak("Buenas noches!")

#Aquí creamos una función para "despertar" a Zoe
def despertar(text):
    ready = ['ey zoe', 'hey zoe', 'ok zoe', 'oye zoe', 'okay zoe'] #Lista de palabras que van a despertar a Zoe

    text = text.lower()

    for phrase in ready:
        if phrase in text:
            return True

    #Devuelve Falso si no encuentra la palabra que hace despertar a Zoe
    return False