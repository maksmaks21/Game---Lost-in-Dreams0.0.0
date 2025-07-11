from kivy.uix.screenmanager import Screen

class SettingsScreen(Screen):
    def go_back(self):
        # Повертаємось до головного меню з анімацією справа наліво
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_menu'
