from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import os

Builder.load_file('./source/kivy_source/statistics_screen.kv')

# класс экрана статистики
# все данные статистики берутся из локального файла в ./../../user/default/statistics.txt
# куда они записаны в формате
# <total_sessions>
# <accuracy>
# <speed>
class StatisticsScreen(Screen):
    total_sessions = 0
    accuracy = 0
    speed = 0

    def __init__(self, **kwargs):
        super(StatisticsScreen, self).__init__(**kwargs)

        # создаем файл статистики, если его нет
        if not os.path.exists('./user/default/statistics.txt'):
            with open('./user/default/statistics.txt', 'w') as f:
                f.write('0\n0\n0')

    def load_screen(self):
        # читаем данные из файла
        with open('./user/default/statistics.txt', 'r') as f:
            self.total_sessions = int(f.readline())
            self.accuracy = float(f.readline())
            self.speed = float(f.readline())

        # обновляем данные на экране
        self.ids.total_sessions.text = 'Всего сессий: ' + str(self.total_sessions)
        self.ids.accuracy.text = 'Точность: ' + str(round(self.accuracy, 2)) + '%'
        self.ids.speed.text = 'Скорость: ' + str(round(self.speed, 2)) + ' зн/мин'

    def reset_statistics(self):
        # обнуляем данные в файле
        with open('./user/default/statistics.txt', 'w') as f:
            f.write('0\n0\n0')
        # обновляем данные на экране
        self.load_screen()

    name = 'statistics_screen'