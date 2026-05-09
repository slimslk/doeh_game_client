from abc import ABC, abstractmethod

import pygame


class DefaultPopupScreen(ABC):

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> str | None:
        pass

    @abstractmethod
    def draw(self):
        pass
