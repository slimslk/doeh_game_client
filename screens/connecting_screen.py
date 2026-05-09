import pygame

from screens.base_screen import BaseScreen
from ws.ws_client import WSClient
from core.config import config
from screens.const.screen_constants import LOGOUT_SCREEN, GAME_SCREEN


class ConnectingScreen(BaseScreen):
    def __init__(self, screen, font, context):
        super().__init__(screen, font, context)

    def handle_event(self, event):
        ws = WSClient(
            url=config.ws_url,
            token=self.context.token,
            on_message=self.context.game_service.apply_server_update
        )
        ws.connect()
        self.context.ws = ws
        if self.context.data:
            if self.context.data == "create":
                ws.send({"action": "create_player", "params": [self.context.selected_character]})
            if self.context.data == "select":
                ws.send({"action": "get_player", "params": [self.context.selected_character]})
        else:
            return {"event": LOGOUT_SCREEN}
        return {"event": GAME_SCREEN}

    def draw(self):
        self.screen.fill((0, 0, 0))
        cx, cy = self.screen.get_rect().center

        connecting = self.font.render("Connecting...", True, (150, 150, 150))
        self.screen.blit(connecting, (cx - 100, cy + 60))

        pygame.display.flip()
