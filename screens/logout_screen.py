import pygame

from screens.base_screen import BaseScreen
from screens.const.screen_constants import START_SCREEN


class LogoutScreen(BaseScreen):
    def handle_event(self, event):
        if self.context.ws:
            self.context.ws.close()
        if self.context.characters:
            self.context.characters = []

        return {"event": START_SCREEN}

    def draw(self):
        self.screen.fill((0, 0, 0))
        cx, cy = self.screen.get_rect().center

        connecting = self.font.render("Logging out...", True, (150, 150, 150))

        self.screen.blit(connecting, (cx - 100, cy + 60))

        pygame.display.flip()
