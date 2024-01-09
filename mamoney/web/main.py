from kivy.app import App
from kivy.uix.widget import Widget

class MaMoney(App):
    pass

class MaMoneyApp(App):
    def build(self):
        return MaMoney()



if __name__ == "__main__":
    MaMoneyApp().run()
    