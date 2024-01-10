import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


user = []
password = []

class MaMoney(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
class Login(BoxLayout):
    def login(self, user, password):
        user_app = {}
        user_app['name'] = user
        user_app['password'] = password
        # self.user_list = []
        # self.password_list = []

class Register(BoxLayout):
    def __init__(self):
        pass

class Income_and_expense(BoxLayout):
    def __init__(self):
        pass    

class Compare_In_and_ex(BoxLayout):
    def __init__(self):
        pass




class moneyApp(App):
    
    
    def build(self):
        login_screen = Screen(name="")
        income_expense_screen = Screen(name="")
        register_screen = Screen(name="")
        compare_screen = Screen (name="")

        sm = ScreenManager()
        
        login_screen.add_widget(Login())
        income_expense_screen.add_widget(Income_and_expense())
        register_screen.add_widget(Register())
        compare_screen.add_widget(Compare_In_and_ex())

        box = BoxLayout(orientation = 'vertical')
        header_label = Label(text="Login", font_size="60sp")
        name_user = TextInput(font_size="30sp")
        password_user = TextInput(font_size="30sp")
        
        

        sm.current = "Log in"
        return sm

if __name__ == "__main__":
    moneyApp().run()

