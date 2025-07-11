from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class CutsceneScreen(Screen):
    def on_enter(self):
        # Коли ми заходимо на цей екран (катсцену), відкладаємо запуск відео на 0.1 секунди,
        # щоб інтерпретатор не завис і відео коректно завантажилось
        Clock.schedule_once(lambda dt: self.play_video('assets/cutscene.mp4'), 0.1)

    def play_video(self, path):
        # Беремо відео віджет за id 'video'
        video = self.ids.get('video')
        if video:
            # Якщо відео вже могло щось грати, то зупиняємо та звільняємо ресурси
            video.state = 'stop'  
            video.unload()        
            video.source = ''     # Очищаємо джерело, щоб "перезавантажити" відео пізніше

            # Через 0.1 секунди намагаємось заново встановити джерело та запустити відео
            Clock.schedule_once(lambda dt: self._reload_video(video, path), 0.1)

    def _reload_video(self, video, path):
        # Встановлюємо шлях до відео і запускаємо його
        video.source = path
        video.state = 'play'

    def skip_cutscene(self):
        # Метод для кнопки "Пропустити" катсцену:
        # Зупиняємо відео та звільняємо ресурси
        video = self.ids.get('video')
        if video:
            video.state = 'stop'
            video.unload()

        # Переходимо назад в ігровий екран або головне меню
        self.manager.transition.direction = 'right'
        self.manager.current = 'game'  # 'game' - це ім'я екрану гри

    def on_leave(self):
        # Коли виходимо з цього екрану, обов’язково зупинити відео,
        # щоб не залишалось фонових процесів відтворення
        video = self.ids.get('video')
        if video:
            video.state = 'stop'
            video.unload()
