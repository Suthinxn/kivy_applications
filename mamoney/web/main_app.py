import kivy
import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Window.clearcolor = 1,1,0,1
class Mamoney_app(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.greeting = ["Have a nice day!",
                         "Good luck.",
                         "Lovely to meet you.",
                         "Wish you all the best.",
                         "Successfully pull off the heist!"]
        

    def random_greeting(self):
        self.random_greet = random.choice(self.greeting)

        print(self.random_greet)
        self.ids.greeting.text = self.random_greet
   


class main(App):
    def build(self):
        return Mamoney_app()
    

if __name__ == '__main__':
    main().run()