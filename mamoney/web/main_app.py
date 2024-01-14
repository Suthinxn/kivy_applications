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

global list_username, list_password
list_username = []
list_password = []

class Register_user(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def check_infomation(self, username, password, confirm_password):

        
        if username in list_username :
            self.ids.topic.text = "This username is already taken!"
            print("This username is already taken!")

        elif len(username) == 0:
            self.ids.topic.text = "Enter your name."
            print("Enter your name.")

        elif len(password) < 8 :
            self.ids.topic.text = "Your password must be not less than 8 characters."
            print("Your password must be not less than 8 characters.") 

        elif confirm_password != password:
            self.ids.topic.text = "Password don't match"
            print("Password don't match")

        if username not in list_username:
            if len(password) >= 6:
                if confirm_password == password:
                    self.ids.topic.text = "Complete"
                    print("Complete")

                    list_username.append(username)
                    list_password.append(password)
                    print("Register succes")
                    print(list_username)
                    print(list_password)
                

class Login_user(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Login= username =>",list_username)
        print("Login= password =>",list_password)

    def check_login(self, username_login, password_login):
        if username_login in list_username:
            index_user = list_username.index(username_login)
            if password_login == list_password[index_user]:
                self.ids.topic_login.text = "Login Succes"
                print("Login Succes")
                print("User", username_login)
                print("Password", list_password[index_user])
            else:
                self.ids.topic_login.text = "Invalid Password."
                print("Invalid Password.")



class Homepage(Screen):
    pass

sum_in = 0
sum_ex = 0

class Income_expense(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def sum_income(self, input_income):
        global sum_in
        sum_in += int(input_income)
        self.ids.display_income.text = str(sum_in)

    def sum_expense(self, input_expense):
        global sum_ex
        sum_ex += int(input_expense)
        self.ids.display_expense.text = str(sum_ex)

kv = Builder.load_file("main.kv")

class main(App):
    def build(self):
        return kv
    

if __name__ == '__main__':
    main().run()