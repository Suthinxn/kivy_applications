import kivy
import random


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class Mamoney(BoxLayout):
    def __init__(self, *args, **kwargs):
        self.text_greeting = ["Have a nice day!",
                              "Good luck",
                              "Have a wonderfulday!",
                              "I wish today is a nice day for you"]
        random_wish = random.choice(self.text_greeting)
        print(random_wish)

class Register(BoxLayout):

class Login(BoxLayout):

class Home(BoxLayout):

class Income_Expense(BoxLayout):

class Save_money(BoxLayout):



class MamoneyApp(App):
    def build(self):



if __name__ == "__main__":
    MamoneyApp().run()

