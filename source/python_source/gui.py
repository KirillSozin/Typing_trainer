from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from source.python_source import start_screen
from source.python_source import trainer_screen
from source.python_source import add_text_screen
from source.python_source import statistics_screen
from source.python_source import result_screen

# изменяем размер экрана
Window.size = (1280, 720)

# изменяем цвет фона экрана
Window.clearcolor = (0.2, 0.2, 0.2, 1)


# класс менеджера экранов
class ScreenManagement(ScreenManager):

    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

        # добавляем экраны
        self.add_widget(start_screen.StartScreen(name='start_screen'))
        self.add_widget(trainer_screen.TrainerScreen(name='trainer_screen'))
        self.add_widget(add_text_screen.AddTextScreen(name='add_text_screen'))
        self.add_widget(statistics_screen.StatisticsScreen(name='statistics_screen'))
        self.add_widget(result_screen.ResultScreen(name='result_screen'))

        # переходим на стартовый экран
        self.current = 'start_screen'


# класс приложения
class MainApp(App):
    def build(self):
        return ScreenManagement()
