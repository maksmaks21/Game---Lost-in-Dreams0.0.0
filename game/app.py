from kivy.app import App # Імпортуємо Kivy App для створення додатку
from kivy.uix.screenmanager import ScreenManager # Імпортуємо ScreenManager для керування екранами
from game.screens.main_menu import MainMenu    # Імпортуємо головний екран меню
from kivy.lang import Builder # Імпортуємо Kivy Builder для завантаження .kv файлів
import os # Імпортуємо необхідні модулі Kivy

from game.screens.settings import SettingsScreen # Імпортуємо екран налаштувань
from game.screens.cutscene import CutsceneScreen # Імпортуємо екран для відтворення відео
from game.screens.game_screen import GameScreen  # Імпортуємо екран гри
from game.screens.gameplay import GameplayScreen # Імпортуємо екран геймплею, якщо він існує
from kivy.uix.widget import Widget  # Імпортуємо Widget для створення віджетів
from kivy.graphics import Color, Rectangle  # Імпортуємо графічні елементи для створення затемнення

class DimOverlay(Widget): # Віджет для затемнення екрану
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Ініціалізуємо батьківський клас
        with self.canvas:  # Додаємо графічні елементи до канвасу
            self.color = Color(0, 0, 0, 0)  # Прозорий чорний
            self.rect = Rectangle(size=self.size, pos=self.pos)  # Прямокутник, який буде заповнювати весь екран
        self.bind(size=self.update_rect, pos=self.update_rect)  # Зв'язуємо зміни розміру та позиції з оновленням прямокутника

    def update_rect(self, *args): # Метод для оновлення розміру та позиції прямокутника
        self.rect.size = self.size # Оновлюємо розмір прямокутника
        self.rect.pos = self.pos # Оновлюємо позицію прямокутника

    def set_opacity(self, value): # Метод для зміни прозорості затемнення
        self.color.a = 1.0 - value  # value: 1.0 (яскраво), 0.1 (тьмяно)

class LostInDreamsApp(App):  # Головний клас додатку (успадковується від Kivy App)
    def build(self): 
        kv_path = os.path.join(os.path.dirname(__file__), '..', 'kv', 'mygame.kv') # Шлях до .kv файлу
        Builder.load_file(kv_path) # Завантажуємо .kv файл, щоб використовувати його в додатку

        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu')) # Додаємо головний екран меню
        sm.add_widget(SettingsScreen(name='settings')) # Додаємо екран налаштувань
        sm.add_widget(CutsceneScreen(name='cutscene')) # Додаємо екран для відтворення відео
        sm.add_widget(GameScreen(name='game'))  # Додаємо екран гри
        sm.add_widget(GameplayScreen(name='gameplay')) # Додаємо екран геймплею, якщо він існує
        return sm # Повертаємо ScreenManager як кореневий віджет додатку

        

def run_game():
    LostInDreamsApp().run()  # Запускається додаток
