from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class MainMenu(Screen):
    def open_settings(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'settings'

    def start_new_game(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'cutscene'

    def start_new_game(self):
        cutscene = self.manager.get_screen('cutscene')
        cutscene.load_video('assets/cutscene.mp4')
        self.manager.transition.direction = 'left'
        self.manager.current = 'cutscene'