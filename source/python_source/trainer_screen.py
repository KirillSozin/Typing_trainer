from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

import os
import random
import time

Builder.load_file('./source/kivy_source/trainer_screen.kv')


def get_random_text():
    # получаем список файлов в директории texts
    texts = os.listdir('./texts')
    # выбираем случайный файл
    text = random.choice(texts)
    # читаем текст из файла
    with open('./texts/' + text, 'r') as f:
        return f.read()


# класс тренировочного экрана
class TrainerScreen(Screen):
    original_text = 'Здесь появится текст'
    current_speed = 0
    current_accuracy = 100

    def __init__(self, **kwargs):
        super(TrainerScreen, self).__init__(**kwargs)
        self.start_time = 0
        self.text = self.original_text

        self.count_letter = 0
        self.count_mistake = 0

    def load_screen(self):
        self.ids.text_for_typing.text = 'Здесь появится текст'
        self.ids.text_for_check.text = ''
        self.ids.current_accuracy.text = 'Точность: 100%'
        self.ids.current_speed.text = 'Скорость: 0 зн/мин'

    def start(self):
        self.original_text = get_random_text()
        self.ids.text_for_typing.text = self.original_text

        self.current_accuracy = 0
        self.current_speed = 0

        self.ids.current_accuracy.text = 'Точность: ' + str(self.current_accuracy) + '%'
        self.ids.current_speed.text = 'Скорость: ' + str(self.current_speed) + ' зн/мин'

        self.count_letter = 0
        self.count_mistake = 0

        self.start_time = time.time()

    # обрабатывает on_text_validate
    def check_text(self, cur_text):

        if len(cur_text) > self.count_letter and cur_text == self.original_text[:len(cur_text)]:
            self.count_letter += 1
            self.ids.text_for_check.text = cur_text
        elif len(cur_text) > self.count_letter:
            self.count_mistake += 1
            self.ids.text_for_check.text = cur_text[:-1]

        self.current_accuracy = max(
            round(((self.count_letter - self.count_mistake) / (self.count_letter + self.count_mistake)) * 100, 2), 0)
        self.ids.current_accuracy.text = 'Точность: ' + str(self.current_accuracy) + '%'

        self.current_speed = round((self.count_letter / (time.time() - self.start_time)) * 60, 2)
        self.ids.current_speed.text = 'Скорость: ' + str(self.current_speed) + ' зн/мин'

        if cur_text == self.original_text:
            self.finish()

    def finish(self):
        self.update_statistict(self.current_accuracy, self.current_speed)
        self.ids.text_for_typing.text = 'Здесь появится текст'
        self.ids.text_for_check.text = ''
        # меняем экран и передаем туда параметры
        self.manager.current = 'result_screen'
        self.manager.get_screen('result_screen').set_result(self.current_accuracy, self.current_speed)

    def update_statistict(self, new_accuracy, new_speed):
        # обновляем статистику
        with open('./user/default/statistics.txt', 'r') as f:
            total_sessions = int(f.readline())
            accuracy = float(f.readline())
            speed = float(f.readline())

        total_sessions += 1
        accuracy = (accuracy * (total_sessions - 1) + new_accuracy) / total_sessions
        speed = (speed * (total_sessions - 1) + new_speed) / total_sessions

        with open('./user/default/statistics.txt', 'w') as f:
            f.write(str(total_sessions) + '\n')
            f.write(str(accuracy) + '\n')
            f.write(str(speed))

    name = 'trainer_screen'
