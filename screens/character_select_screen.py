import pygame

from core.context import AppContext
from screens.base_screen import BaseScreen


class CharacterSelectScreen(BaseScreen):
    def __init__(self, screen, font, context: AppContext):
        super().__init__(screen, font, context)
        chars = context.connector.get_characters()

        # временные данные
        if not context.characters:
            context.characters = ["Warrior", "Mage", "Rogue"]

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

        elif event.key == pygame.K_RETURN:
            self.context.selected_character = self.context.characters[self.selected]
            return {
                "event": "character_selected",
                "data": {"selected_character": self.context.selected_character}
            }

        elif event.key == pygame.K_n:
            self.create_mode = True

        elif event.key == pygame.K_BACKSPACE and self.create_mode:
            self.new_name = self.new_name[:-1]

        elif event.key == pygame.K_ESCAPE:
            return {"event": "logout"}

        elif self.create_mode:
            if event.key == pygame.K_RETURN and self.new_name:
                self.context.characters.append(self.new_name)
                self.new_name = ""
                self.create_mode = False
            else:
                self.new_name += event.unicode

    def draw(self):
        self.screen.fill((0, 0, 0))
        w, h = self.screen.get_size()

        # список персонажей
        for i, char in enumerate(self.context.characters):
            color = (0, 200, 0) if i == self.selected else (200, 200, 200)
            text = self.font.render(char, True, color)
            self.screen.blit(text, (50, 50 + i * 30))

        # статистика (заглушка)
        stats = [
            f"Name: {self.context.characters[self.selected]}",
            "HP: 100",
            "STR: 10",
            "AGI: 8"
        ]

        for i, line in enumerate(stats):
            t = self.font.render(line, True, (180, 180, 180))
            self.screen.blit(t, (300, 60 + i * 30))

        # создание персонажа
        create = self.font.render("N - New character:", True, (150, 150, 150))
        self.screen.blit(create, (50, h - 80))

        name = self.font.render(self.new_name, True, (255, 255, 255))
        pygame.draw.rect(self.screen, (80, 80, 80), (220, h - 85, 200, 30), 2)
        self.screen.blit(name, (225, h - 80))

        pygame.display.flip()
