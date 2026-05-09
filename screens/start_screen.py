import pygame

from screens.base_screen import BaseScreen

from screens.const.screen_constants import LOGIN_SCREEN, REGISTER_SCREEN


class StartScreen(BaseScreen):
    MENU_ITEMS = ["Login", "Register", "Quit"]
    _BANNER_PATH = "assets/banner/banner.png"

    ASCII_ART = [
        "██████╗  ██████╗ ███████╗██╗  ██╗",
        "██╔══██╗██╔═══██╗██╔════╝██║  ██║",
        "██║  ██║██║   ██║█████╗  ███████║",
        "██║  ██║██║   ██║██╔══╝  ██╔══██║",
        "██████╔╝╚██████╔╝███████╗██║  ██║",
        "╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝",
        "░▒▓█  Domains of Endless Hunger  █▓▒░",
    ]

    selected_index = 0

    def __init__(self, screen, font, context):
        super().__init__(screen, font, context)

        self.logo = pygame.image.load(self._BANNER_PATH).convert_alpha()

        max_width, max_height = screen.get_size()
        iw, ih = self.logo.get_size()

        scale = min(max_width / iw, max_height / ih)

        new_size = (int(iw * scale), int(ih * scale))

        self.logo = pygame.transform.scale(self.logo, new_size)

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
                    return {"event": LOGIN_SCREEN}
                if selected_item == "Register":
                    return {"event": REGISTER_SCREEN}

                else:
                    raise KeyboardInterrupt

    def draw(self):
        self.screen.fill((0, 0, 0))
        w, h = self.screen.get_size()

        logo_rect = self.logo.get_rect(center=(w // 2, 150))
        self.screen.blit(self.logo, logo_rect)

        menu_start_y = h // 2 + 50
        for i, item in enumerate(self.MENU_ITEMS):
            color = (255, 255, 0) if i == self.selected_index else (255, 255, 255)
            text_surface = self.font.render(item, True, color)
            self.screen.blit(text_surface, (w // 2 - text_surface.get_width() // 2, menu_start_y + i * 50))

        pygame.display.flip()
