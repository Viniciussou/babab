from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
    pass

class LogApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Yellow"
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Builder.load_file('kvcódigos/login.kv'))
        return self.screen_manager
    
if __name__ == "__main__":
    app = LogApp()
    app.run()