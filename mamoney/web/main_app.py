import kivy
import random

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


# Window.clearcolor = 1,1,0,1
class WindowManager(ScreenManager):
    pass

class Mamoney_app(Screen):
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



class Register_user(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_username = ["Den"]
        self.list_password = []
    
    def check_infomation(self, username, password, confirm_password):

        if username in self.list_username :
            self.ids.topic.text = "This username is already taken!"
            print("This username is already taken!")

        if len(password) < 6 :
            self.ids.topic.text = "Your password must be not less than 8 characters."
            print("Your password must be not less than 8 characters.") 

        if confirm_password != password:
            self.ids.topic.text = "Password don't match"
            print("Password don't match")

        if username not in self.list_username:
            self.ids.topic.text = "Complete"
            print("Complete")
class Login_user(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
kv = Builder.load_file("main.kv")

class main(App):
    def build(self):
        return kv
    

if __name__ == '__main__':
    main().run()