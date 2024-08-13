from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from inicializadores.sublogin import SubApp as SubLoginApp
from inicializadores.login import LogApp as LoginApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.primary_palette = "Yellow" 
        self.theme_cls.primary_palette = self.primary_palette

        self.sublogin_app = SubLoginApp()
        self.login_app = LoginApp()

if __name__ == "__main__":
    app = MainApp()
    app.run()