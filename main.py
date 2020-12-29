import funciones
from kivymd.app import MDApp
from kivy.core.window import Window
from threading import Thread


Window.size = (300, 500) #Temporalmente durante el desarrollo de la app


class Zoe(MDApp):
    def screen_settings(self):
        self.screen_manager.current = 'settings'

    def night_mode(self, checkbox,value):
        if value:
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def wake_up(self):
        t2 = Thread(target=funciones.ejecutar)
        t2.start()

    def escuchando():
        while True:
            print("Escuchando...")
            text = funciones.get_audio().lower()

            if funciones.despertar(text) == True:
                funciones.ejecutar()

    t1 = Thread(target=escuchando)
    t1.daemon = True
    t1.start()


Zoe().run()



