import funciones, requests
from kivymd.app import MDApp
from kivy.core.window import Window
from threading import Thread


Window.size = (300, 500) #Temporalmente durante el desarrollo de la app


class Zoe(MDApp):
    def on_start(self):
        t1 = Thread(target=Zoe.escuchando, args=(self,))
        t1.start()

    def screen_settings(self):
        self.screen_manager.current = 'settings'

    def night_mode(self, checkbox,value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def wake_up(self):
        t2 = Thread(target=Zoe.ejecutar, args=(self,))
        t2.start()

    def clima(self):
        api_address = 'https://api.weatherbit.io/v2.0/current?key=ec9c825a578f4e9b8ce68b321d331b84&lang=es&city='
        funciones.speak("Dime el nombre de la ciudad")
        print("Escuchando...")
        city = funciones.get_audio()

        Zoe.ciudad(self, city)

        url = api_address + city
        respuesta = requests.get(url)
        clima = respuesta.json()

        datos_clima = city + " ahora mismo está " + clima['data'][0]['weather'][
            'description'] + " . La temperatura actualmente es de" + str(
            clima['data'][0]['temp']) + "grados"

        funciones.speak(datos_clima)

    def ciudad(self, city):
        ciudadSeleccionada = city.upper()
        txtCiudad = self.root.ids.txtCiudad
        txtCiudad.text = ciudadSeleccionada

    def escuchando(self):
        while True:
            print("Escuchando...")
            text = funciones.get_audio().lower()

            if funciones.despertar(text) == True:
                Zoe.ejecutar(self)

    def ejecutar(self):
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
                    Zoe.clima(self)

            exit_strs = ["apágate zoe", "adiós zoe"]
            for phrase in exit_strs:
                if phrase in text:
                    funciones.speak("Hasta luego")
                    return False

        except:
            funciones.speak("Repite de nuevo porfavor")

Zoe().run()


