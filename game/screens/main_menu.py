from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class MainMenu(Screen):
    def open_settings(self):
        # Переходимо на екран налаштувань з анімацією зліва направо
        self.manager.transition.direction = 'left'
        self.manager.current = 'settings'

    def start_new_game(self):
        # Метод, що запускається при натисканні "Нова гра"
        # Отримуємо екран катсцени
        cutscene = self.manager.get_screen('cutscene')
        
        # Викликаємо метод завантаження і запуску відео
        cutscene.play_video('assets/cutscene.mp4')

        # Переходимо до катсцени з анімацією переходу зліва направо
        self.manager.transition.direction = 'left'
        self.manager.current = 'cutscene'
        
