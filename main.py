import funciones
from kivymd.app import MDApp
from kivy.core.window import Window
from threading import Thread


Window.size = (300, 500) #Temporalmente durante el desarrollo de la app
boton_despertar = False


class Zoe(MDApp):
    def screen_settings(self):
        self.screen_manager.current = 'settings'

    def night_mode(self, checkbox,value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def wake_up(self):
        boton_despertar = True
        return boton_despertar

    def escuchando():
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
                            return False

                except:
                    funciones.speak("Repite de nuevo porfavor")

    t1 = Thread(target=escuchando)
    t1.daemon = True
    t1.start()


Zoe().run()



