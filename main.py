import funciones
import kivy
from kivy.app import App
from kivy.uix.widget import Widget


class Contenedor(Widget):
    pass

class ZoeApp(App):
    def build(self):
        return Contenedor()

if __name__ == "__main__":
    ZoeApp().run()


'''
while True:
    print("Escuchando...")
    text = funciones.get_audio().lower()

    if funciones.despertar(text) == True:
        funciones.saludo()
        funciones.speak("¿En qué puedo ayudarte?")
        print("Escuchando...")
        try:
            text = funciones.get_audio()

            saludo_strs = ["hola", "saludos"]
            for phrase in saludo_strs:
                if phrase in text:
                    funciones.speak("¿Hola, como estás?")

            nombre_strs = ["cómo te llamas", "cuál es tu nombre"]
            for phrase in nombre_strs:
                if phrase in text:
                    funciones.speak("Me llamo Zoe")

            clima_strs = ["dime el tiempo", "dime el clima"]
            for phrase in clima_strs:
                if phrase in text:
                    funciones.clima()

            exit_strs = ["apágate zoe", "adiós zoe"]
            for phrase in exit_strs:
                if phrase in text:
                    funciones.speak("Hasta luego")
                    break

        except:
            funciones.speak("Repite de nuevo porfavor")
'''