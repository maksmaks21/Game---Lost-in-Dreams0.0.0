from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color

GRAVITY = -0.5

class Player(Widget):
    velocity_y = NumericProperty(0)
    on_ground = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (50, 80)
        self.pos = (100, 100)
        with self.canvas:
            Color(0, 1, 0)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
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
