from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color

GRAVITY = -0.5  # сила гравітації (швидкість падіння)

class Player(Widget):
    velocity_y = NumericProperty(0)  # вертикальна швидкість (висота стрибка/падіння)
    on_ground = False  # прапорець - чи стоїть гравець на землі

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = (50, 80)  # розмір гравця
        self.pos = (100, 100)  # початкова позиція
        # Малюємо прямокутник зеленого кольору замість спрайту
        with self.canvas:
            Color(0, 1, 0)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        # Оновлюємо положення 60 разів на секунду
        Clock.schedule_interval(self.update, 1/60)

    def update(self, dt):
        # Якщо гравець у повітрі, застосовуємо гравітацію
        if not self.on_ground:
            self.velocity_y += GRAVITY
            self.y += self.velocity_y
            # Перевіряємо, чи не впав на "землю"
            if self.y <= 100:
                self.y = 100
                self.velocity_y = 0
                self.on_ground = True
        # Оновлюємо позицію прямокутника, щоб він рухався разом з гравцем
        self.rect.pos = self.pos

    def jump(self):
        # Стрибок можливий, якщо гравець стоїть на землі
        if self.on_ground:
            self.velocity_y = 15  # задаємо початкову швидкість вгору
            self.on_ground = False
