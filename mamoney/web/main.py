import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
# from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MaMoney(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def login(self, user, password):
        user_app = {}
        user_app['name'] = user
        user_app['password'] = password
        # self.user_list = []
        # self.password_list = []
class Login(BoxLayout):
    


class moneyApp(App):
    def build(self):
        return MaMoney()


if __name__ == "__main__":
    moneyApp().run()

