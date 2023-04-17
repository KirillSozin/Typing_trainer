from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('./source/kivy_source/result_screen.kv')


# класс экрана результата
class ResultScreen(Screen):
    accuracy = 0.0
    speed = 0.0

    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)

    def set_result(self, accuracy, speed):
        self.accuracy = accuracy
        self.speed = speed
        # обновляем данные на экране
        self.ids.accuracy.text = 'Точность: ' + str(accuracy) + '%'
        self.ids.speed.text = 'Скорость: ' + str(speed) + ' зн/мин'

    name = 'result_screen'
