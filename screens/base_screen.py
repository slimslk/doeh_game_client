from abc import ABC, abstractmethod


class BaseScreen(ABC):
    def __init__(self, screen, font, context):
        self.screen = screen
        self.font = font
        self.context = context

    @abstractmethod
    def handle_event(self, event):
        """
        return:
        {
            "event": "some_event",
            "data": {...}
        }
        """
        pass

    @abstractmethod
    def draw(self):
        """Рисует экран"""
        pass

    def on_enter(self):
        """Вызывается при показе экрана"""
        pass

    def on_exit(self):
        """Вызывается при уходе с экрана"""
        pass