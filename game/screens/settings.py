from kivy.uix.screenmanager import Screen # Імпортуємо Screen з Kivy для створення екранів
from kivy.core.audio import SoundLoader # Імпортуємо SoundLoader для завантаження звуків
import json # Імпортуємо json для роботи з файлами налаштувань
import os # Імпортуємо os для роботи з файловою системою
from kivy.core.audio import Sound # Імпортуємо Sound для роботи зі звуками
from kivy.app import App # Імпортуємо Kivy App для доступу до додатку

SETTINGS_PATH = "settings.json"

class SettingsScreen(Screen): # Екран налаштувань

    def on_brightness_change(self, value):
        print(f"Яскравість змінено на {value}") # Лог для відстеження зміни яскравості
        app = App.get_running_app() # Отримуємо поточний додаток
        if hasattr(app, 'dim_overlay'): # Перевіряємо, чи є у додатку затемнення
            app.dim_overlay.set_opacity(value) # Змінюємо прозорість затемнення

    def on_pre_enter(self):
        self.load_settings() # Завантажуємо налаштування перед входом на екран

    def save_settings(self):
        data = { # Збираємо налаштування з віджетів
            'volume': self.ids.volume_slider.value,
            'brightness': self.ids.brightness_slider.value,
            'language': self.ids.language_spinner.text,
            'fullscreen': self.ids.fullscreen_checkbox.active
        }
        with open(SETTINGS_PATH, 'w', encoding='utf-8') as f: # Записуємо налаштування у файл
            json.dump(data, f, indent=4) # Форматуємо JSON для читабельності

    def load_settings(self):    # Завантажуємо налаштування з файлу
        if os.path.exists(SETTINGS_PATH): # Перевіряємо, чи існує файл налаштувань
            with open(SETTINGS_PATH, 'r', encoding='utf-8') as f: # Відкриваємо файл для читання
                data = json.load(f) # Завантажуємо дані з JSON
                self.ids.volume_slider.value = data.get('volume', 0.5) # Встановлюємо гучність, якщо вона є, або 0.5 за замовчуванням
                self.ids.brightness_slider.value = data.get('brightness', 1) # Встановлюємо яскравість, якщо вона є, або 1 за замовчуванням
                self.ids.language_spinner.text = data.get('language', 'Українська') # Встановлюємо мову, якщо вона є, або 'Українська' за замовчуванням
                self.ids.fullscreen_checkbox.active = data.get('fullscreen', False) # Встановлюємо повноекранний режим, якщо він є, або False за замовчуванням


    def on_volume_change(self, value): 
        print(f"[Налаштування] Гучність змінено: {value}") # Лог для відстеження зміни гучності
        
        # Якщо ти маєш окремі звуки, треба кожному задати volume
        if hasattr(self, 'sound') and self.sound:
            self.sound.volume = value

        # Якщо у тебе є video плеєр:
        if 'video' in self.ids:
            self.ids.video.volume = value  # Працює з ffpyplayer

    def on_brightness_change(self, value):
        # 💡 Просто зберігаємо значення, бо Kivy не змінює системну яскравість
        print(f'Яскравість змінено на {value}')
        self.save_settings()
