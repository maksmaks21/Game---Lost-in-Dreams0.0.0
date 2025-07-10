from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

class CutsceneScreen(Screen):
    def on_kv_post(self, base_widget):
        # Після завантаження .kv прив'язуємо id video до self.video
        self.video = self.ids.video

    def load_video(self, video_path):
        self.video.source = video_path
        self.video.state = 'play'

    def on_enter(self):
        # Запускаємо відео автоматично при вході (опційно)
        if self.video.source:
            Clock.schedule_once(lambda dt: setattr(self.video, 'state', 'play'), 0.1)

        def skip_cutscene(self):
            # Наприклад, перейти назад в меню або в гру
            self.manager.current = 'game'
            self.manager.transition.direction = 'right' 
