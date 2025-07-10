from kivy.app import App # Імпортуємо Kivy App для створення додатку
from kivy.uix.screenmanager import ScreenManager # Імпортуємо ScreenManager для керування екранами
from game.screens.main_menu import MainMenu    # Імпортуємо головний екран меню
from kivy.lang import Builder # Імпортуємо Kivy Builder для завантаження .kv файлів
import os # Імпортуємо необхідні модулі Kivy

from game.screens.settings import SettingsScreen # Імпортуємо екран налаштувань
from game.screens.cutscene import CutsceneScreen # Імпортуємо екран для відтворення відео
from game.screens.game_screen import GameScreen  # Імпортуємо екран гри
from game.screens.gameplay import GameplayScreen # Імпортуємо екран геймплею, якщо він існує

class LostInDreamsApp(App):  # Головний клас додатку (успадковується від Kivy App)
    def build(self):
        kv_path = os.path.join(os.path.dirname(__file__), '..', 'kv', 'mygame.kv')
        Builder.load_file(kv_path)

        sm = ScreenManager()
        sm.add_widget(MainMenu(name='main_menu')) # Додаємо головний екран меню
        sm.add_widget(SettingsScreen(name='settings')) # Додаємо екран налаштувань
        sm.add_widget(CutsceneScreen(name='cutscene')) # Додаємо екран для відтворення відео
        sm.add_widget(GameScreen(name='game'))  # Додаємо екран гри
        sm.add_widget(GameplayScreen(name='gameplay')) # Додаємо екран геймплею, якщо він існує
        return sm

def run_game():
    LostInDreamsApp().run()  # Запускається додаток
