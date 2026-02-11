import pygame

from screens.base_screen import BaseScreen


class StartScreen(BaseScreen):
    MENU_ITEMS = ["Login", "Register", "Quit"]

    ASCII_ART = [
        "  ____  _             _        ",
        " / ___|| |_ __ _ _ __| |_ ___  ",
        " \___ \| __/ _` | '__| __/ _ \ ",
        "  ___) | || (_| | |  | ||  __/ ",
        " |____/ \__\__,_|_|   \__\___| ",
    ]

    selected_index = 0

    def __init__(self, screen, font, context):
        super().__init__(screen, font, context)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            raise KeyboardInterrupt
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_index = (self.selected_index - 1) % len(self.MENU_ITEMS)
            elif event.key == pygame.K_DOWN:
                self.selected_index = (self.selected_index + 1) % len(self.MENU_ITEMS)
            elif event.key == pygame.K_RETURN:
                selected_item = self.MENU_ITEMS[self.selected_index]
                if selected_item == "Login":
                    return {"event": "login"}
                if selected_item == "Register":
                    return {"event": "register"}

                else:
                    raise KeyboardInterrupt

    def draw(self):
        self.screen.fill((0, 0, 0))  # фон черный
        w, h = self.screen.get_size()

        # --- Отображение ASCII art ---
        start_y = 50  # отступ сверху
        for i, line in enumerate(self.ASCII_ART):
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text_surface, (w // 2 - text_surface.get_width() // 2, start_y + i * 30))

        # --- Отображение меню ---
        menu_start_y = h // 2 + 50
        for i, item in enumerate(self.MENU_ITEMS):
            color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)
            text_surface = self.font.render(item, True, color)
            self.screen.blit(text_surface, (w // 2 - text_surface.get_width() // 2, menu_start_y + i * 50))

        pygame.display.flip()
