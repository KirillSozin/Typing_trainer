from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import os
import re

Builder.load_file('./source/kivy_source/add_text_screen.kv')


# класс экрана добавления текста
class AddTextScreen(Screen):
    def __init__(self, **kwargs):
        super(AddTextScreen, self).__init__(**kwargs)

    def add_text(self):
        # получаем текст
        text = self.ids.text_input.text

        # проверяем на пустоту
        if text == '':
            return

        # форматируем текст
        text = self.format_text(text)

        # добавляем новый файл в директорию texts с названием text<n+1>.txt
        # где n - количество файлов в директории texts
        # считаем количество файлов в директории
        n = len(os.listdir('./texts'))
        # создаем файл
        with open('./texts/text' + str(n + 1) + '.txt', 'w') as f:
            f.write(text)

        # очищаем поле ввода
        self.ids.text_input.text = ''

    # обрабатываем текст чтобы не было неожиданностей в виде странных символов
    def format_text(self, text):
        # удаляем странные символы
        text = re.sub('[^a-zA-Zа-яА-Я0-9.,!? :-;]', '', text)
        # удаляем переносы строк
        text = re.sub('\n', ' ', text)
        text = re.sub('\r', ' ', text)
        # удаляем лишние пробелы
        text = re.sub('\s+', ' ', text)
        return text

    def load_screen(self):
        # очищаем поле ввода
        self.ids.text_input.text = ''

    name = 'add_text_screen'
