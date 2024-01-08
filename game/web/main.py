import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window 

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down = self._on_key_down)

        with self.canvas:
            Rectangle(
                source = 'image/dinosaur.gif',
                pos = (0, 0),
                size = (228/2, 228/2)
            )
    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self._on_key_down)
        self._keyboard = None
    
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        print('key down', text)

    

class MyApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    MyApp().run()
