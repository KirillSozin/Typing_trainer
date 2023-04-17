from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('./source/kivy_source/start_screen.kv')


# класс стартового экрана
class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

    name = 'start_screen'

    def go_to_trainer(self):
        self.manager.current = 'trainer_screen'
        # подготавливаем экран тренировки
        self.manager.get_screen('trainer_screen').load_screen()

    def go_to_add_text(self):
        self.manager.current = 'add_text_screen'
        # подготавливаем экран добавления текста
        self.manager.get_screen('add_text_screen').load_screen()

    def go_to_statistics(self):
        self.manager.current = 'statistics_screen'
        # подготавливаем экран статистики
        self.manager.get_screen('statistics_screen').load_screen()

