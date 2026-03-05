import httpx
import pygame

from connector.server_connector import ServerConnector
from errors.response_errors import DefaultResponseError, UserNotFoundError, AuthenticationError
from screens.base_screen import BaseScreen


class LoginScreen(BaseScreen):
    def __init__(self, screen, font, context):
        super().__init__(screen, font, context)

        self.fields = ["login", "password"]
        self.active_index = 0

        self.login_text = ""
        self.password_text = ""
        self.error = ""

    @property
    def active_field(self):
        return self.fields[self.active_index]

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_TAB:
            self.active_index = (self.active_index + 1) % len(self.fields)

        elif event.key == pygame.K_BACKSPACE:
            if self.active_field == "login":
                self.login_text = self.login_text[:-1]
            else:
                self.password_text = self.password_text[:-1]

        elif event.key == pygame.K_RETURN:
            if self.login_text and self.password_text:
                try:
                    response = self.context.connector.login(self.login_text, self.password_text)
                    self.context.token = response.get("Authorization")
                    self.context.user = self.login_text
                    return {
                        "event": "login_success",
                        "data": response,
                    }
                except DefaultResponseError as e:
                    if e.__class__.__name__ in ["AuthenticationError", "UserNotFoundError"]:
                        self.error = "Invalid credentials"
                    else:
                        self.error = "Opps. Something went wrong"

            else:
                self.error = "Login and password required"

        elif event.key == pygame.K_ESCAPE:
            return {"event": "start"}

        else:
            char = event.unicode
            if self.active_field == "login":
                self.login_text += char
            else:
                self.password_text += char

    def draw(self):
        self.screen.fill((0, 0, 0))
        cx, cy = self.screen.get_rect().center

        self._draw_field("Login", self.login_text, cx, cy - 40, self.active_field == "login")
        self._draw_field("Password", "*" * len(self.password_text), cx, cy, self.active_field == "password")

        register = self.font.render("Press ESC to Main Menu", True, (150, 150, 150))
        self.screen.blit(register, (cx - 100, cy + 60))

        if self.error:
            err = self.font.render(self.error, True, (200, 50, 50))
            self.screen.blit(err, (cx - 120, cy + 100))

        pygame.display.flip()

    def _draw_field(self, label, value, x, y, active):
        label_surf = self.font.render(f"{label}:", True, (200, 200, 200))
        value_surf = self.font.render(value, True, (255, 255, 255))

        self.screen.blit(label_surf, (x - 220, y))
        pygame.draw.rect(self.screen, (0, 200, 0) if active else (80, 80, 80),
                         (x - 100, y, 200, 30), 2)
        self.screen.blit(value_surf, (x - 95, y + 5))
