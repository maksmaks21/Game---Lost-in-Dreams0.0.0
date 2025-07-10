from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color

GRAVITY = -0.5  # Гравітація

class Player(Widget):
    velocity_y = NumericProperty(0)  # Швидкість по вертикалі
    on_ground = False # Чи на землі

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (50, 80)
        self.pos = (100, 100)
        with self.canvas:
            Color(0, 1, 0)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        Clock.schedule_interval(self.update, 1.0 / 60.0)  # 60 FPS

    def update(self, dt):
        # гравітація
        if not self.on_ground:
            self.velocity_y += GRAVITY
            self.y += self.velocity_y
            if self.y <= 100:
                self.y = 100
                self.velocity_y = 0
                self.on_ground = True

        self.rect.pos = self.pos

    def jump(self):
        if self.on_ground:
            self.velocity_y = 15
            self.on_ground = False

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player = Player()
        self.add_widget(self.player)
        Window.bind(on_key_down=self.on_key_down)

    def on_key_down(self, window, key, *args):
        if key == 276:  # left
            self.player.x -= 20
        elif key == 275:  # right
            self.player.x += 20
        elif key == 32:  # space
            self.player.jump()