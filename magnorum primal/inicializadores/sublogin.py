from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class Screen1(MDScreen):
    pass

class SubApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Yellow"
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Builder.load_file('kvcódigos/sublogin.kv'))
        return self.screen_manager

    def theme(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'
            
            
if __name__ == "__main__":
    app = SubApp()
    app.run()