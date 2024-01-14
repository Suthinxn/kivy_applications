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
        self.list_password = ["123456789"]
    
    def check_infomation(self, username, password, confirm_password):

        if username in self.list_username :
            self.ids.topic.text = "This username is already taken!"
            print("This username is already taken!")

        elif len(username) == 0:
            self.ids.topic.text = "Enter your name."
            print("Enter your name.")

        elif len(password) < 6 :
            self.ids.topic.text = "Your password must be not less than 8 characters."
            print("Your password must be not less than 8 characters.") 

        elif confirm_password != password:
            self.ids.topic.text = "Password don't match"
            print("Password don't match")

        if username not in self.list_username:
            if len(password) >= 6:
                if confirm_password == password:
                    self.ids.topic.text = "Complete"
                    print("Complete")

                    self.list_username.append(username)
                    self.list_password.append(password)
                    print("Register succes")
                    print(self.list_username)
                    print(self.list_password)

    def database_usernaem(self):
        return self.list_username 
    def database_password(self):
        return self.list_password
class Login_user(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_register = Register_user()
        self.list_username_login = self.class_register.database_usernaem()
        self.list_password_login = self.class_register.database_password()

    def check_login(self, username_login, password_login):
        if username_login in self.list_username_login:
            index_user = self.list_username_login.index(username_login)
            if password_login == self.list_password_login[index_user]:
                self.ids.topic_login.text = "Login Succes"
                print("Login Succes")
            else:
                self.ids.topic_login.text = "Invalid Password."
                print("Tnvalid Password.")
        print(self.list_username_login)
        print(self.list_password_login)

kv = Builder.load_file("main.kv")

class main(App):
    def build(self):
        return kv
    

if __name__ == '__main__':
    main().run()