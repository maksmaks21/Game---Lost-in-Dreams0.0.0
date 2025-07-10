from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from game.widgets.player import Player

from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from game.widgets.player import Player

class GameplayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player = Player()
        self.add_widget(self.player)
        Window.bind(on_key_down=self.on_key_down)

    def on_key_down(self, window, key, *args):
        if key == 276:  # стрілка вліво
            self.player.x -= 20
        elif key == 275:  # стрілка вправо
            self.player.x += 20
        elif key == 32:  # пробіл - стрибок
            self.player.jump()
