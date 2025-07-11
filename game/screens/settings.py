from kivy.uix.screenmanager import Screen

class SettingsScreen(Screen):
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_menu'