import pygame

from core.context import AppContext
from screens.base_screen import BaseScreen
from screens.const.screen_constants import CONNECT_SCREEN, LOGOUT_SCREEN


class CharacterSelectScreen(BaseScreen):
    def __init__(self, screen, font, context: AppContext):
        super().__init__(screen, font, context)
        chars = context.connector.get_characters()

        if chars:
            context.characters = [char.get("name", "Default") for char in chars]

        self.selected = 0
        self.new_name = ""
        self.create_mode = False

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:
            self.selected = max(0, self.selected - 1)

        elif event.key == pygame.K_DOWN:
            self.selected = min(len(self.context.characters) - 1, self.selected + 1)

        elif event.key == pygame.K_RETURN and not self.create_mode:
            self.context.selected_character = self.context.characters[self.selected]
            return {
                "event": CONNECT_SCREEN,
                "data": {"data": "select"}
            }

        elif event.key == pygame.K_n and not self.create_mode:
            self.create_mode = True

        elif event.key == pygame.K_BACKSPACE and self.create_mode:
            self.new_name = self.new_name[:-1]

        elif event.key == pygame.K_ESCAPE:
            return {"event": LOGOUT_SCREEN}

        elif self.create_mode:
            if event.key == pygame.K_RETURN and self.new_name:
                self.context.selected_character = self.new_name
                return {
                    "event": CONNECT_SCREEN,
                    "data": {"data": "create"}
                }
            else:
                self.new_name += event.unicode

    def draw(self):
        self.screen.fill((0, 0, 0))
        w, h = self.screen.get_size()

        for i, char in enumerate(self.context.characters):
            color = (0, 200, 0) if i == self.selected else (200, 200, 200)
            text = self.font.render(char, True, color)
            self.screen.blit(text, (50, 50 + i * 30))
        create = self.font.render("n - New character:", True, (150, 150, 150))
        self.screen.blit(create, (50, h - 80))
        if self.create_mode:
            name = self.font.render(self.new_name, True, (255, 255, 255))
            pygame.draw.rect(self.screen, (80, 80, 80), (w/2-100, h/2 - 85, 200, 30), 2)
            self.screen.blit(name, (w/2-100, h/2 - 80))

        pygame.display.flip()
