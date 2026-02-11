import httpx
import pygame

from connector.server_connector import ServerConnector
from screens.base_screen import BaseScreen


class RegisterScreen(BaseScreen):
    def __init__(self, screen, font, context):
        super().__init__(screen, font, context)

        self.fields = ["login", "password", "repeat"]
        self.active_index = 0

        self.login_text = ""
        self.password_text = ""
        self.repeat_text = ""
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
            self._backspace()

        elif event.key == pygame.K_RETURN:
            if not self.login_text or not self.password_text:
                self.error = "All fields required"
            elif self.password_text != self.repeat_text:
                self.error = "Passwords do not match"
            else:
                response = self.context.connector.register_user(self.login_text, self.password_text)
                return {
                    "event": "login_success",
                    "data": response,
                }

        elif event.key == pygame.K_ESCAPE:
            return {"event": "start"}

        else:
            self._add_char(event.unicode)

    def draw(self):
        self.screen.fill((0, 0, 0))
        cx, cy = self.screen.get_rect().center

        self._draw_field("Login", self.login_text, cx, cy - 60, self.active_field == "login")
        self._draw_field("Password", "*" * len(self.password_text), cx, cy - 20, self.active_field == "password")
        self._draw_field("Repeat", "*" * len(self.repeat_text), cx, cy + 20, self.active_field == "repeat")

        back = self.font.render("ESC - Back to Main Menu", True, (150, 150, 150))
        self.screen.blit(back, (cx - 120, cy + 70))

        if self.error:
            err = self.font.render(self.error, True, (200, 50, 50))
            self.screen.blit(err, (cx - 140, cy + 110))

        pygame.display.flip()

    def _add_char(self, char):
        if self.active_field == "login":
            self.login_text += char
        elif self.active_field == "password":
            self.password_text += char
        else:
            self.repeat_text += char

    def _backspace(self):
        if self.active_field == "login":
            self.login_text = self.login_text[:-1]
        elif self.active_field == "password":
            self.password_text = self.password_text[:-1]
        else:
            self.repeat_text = self.repeat_text[:-1]

    def _draw_field(self, label, value, x, y, active):
        label_surf = self.font.render(f"{label}:", True, (200, 200, 200))
        value_surf = self.font.render(value, True, (255, 255, 255))

        self.screen.blit(label_surf, (x - 220, y))
        pygame.draw.rect(self.screen, (0, 200, 0) if active else (80, 80, 80),
                         (x - 100, y, 200, 30), 2)
        self.screen.blit(value_surf, (x - 95, y + 5))
