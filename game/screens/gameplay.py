from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from game.widgets.player import Player  # Імпорт класу гравця

class GameplayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Створюємо гравця і додаємо його на екран
        self.player = Player()
        self.add_widget(self.player)
        # Підписуємося на події клавіатури для керування гравцем
        Window.bind(on_key_down=self.on_key_down)

    def on_key_down(self, window, key, *args):
        # Обробляємо натискання клавіш
        if key == 276:  # стрілка вліво
            self.player.x -= 20
        elif key == 275:  # стрілка вправо
            self.player.x += 20
        elif key == 32:  # пробіл - стрибок
            self.player.jump()
