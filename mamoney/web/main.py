import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
# from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MaMoney(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def login(self):
        pass

class moneyApp(App):
    def build(self):
        return MaMoney()


if __name__ == "__main__":
    moneyApp().run()

