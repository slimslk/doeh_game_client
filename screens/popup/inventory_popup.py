import pygame

from screens.popup.popup_factory import PopupFactory


@PopupFactory.register('inventory')
class InventoryPopupScreen:
    def __init__(
            self,
            screen: pygame.Surface,
            font: pygame.font.Font,
            inventory
    ):
        self.screen = screen
        self.font = font
        self.inventory = inventory
        self._selected = 0
        self._min_width = 15 * self.font.size("=")[0]
        self._min_height = 9 * self.font.size("=")[1]
        self.rect = pygame.Rect(100,100,
            # self.screen.get_size()[0] - self._min_width // 2,
            # self.screen.get_size()[1] - self._min_height // 2,
            self._min_width, self._min_height
        )

    def handle_event(self, event: pygame.event.Event) -> dict | str | None:
        if event.type != pygame.KEYDOWN:
            return None

        if event.key in (pygame.K_UP, pygame.K_w):
            self._selected = (self._selected - 1) % len(self.inventory)

        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self._selected = (self._selected + 1) % len(self.inventory)

        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            return {"action": "use_item", "params": [self._selected]}

        return None

    def draw(self):
        shift_y = 0
        screen_size = self.screen.get_size()
        self.draw_back_screen_overlay(screen_size)
        rect = pygame.draw.rect(self.screen, (0, 0, 0), self.rect, border_radius=12)

        page_size = 5

        start = max(0, self._selected - page_size + 1)
        end = start + page_size

        for index, item in enumerate(self.inventory[start:end]):
            if start + index == self._selected:
                text_img = self.font.render(f"-> {item}", True, (255, 255, 255))
            else:
                text_img = self.font.render(f"{item}", True, (255, 255, 255))
            text_rect = text_img.get_rect(center=(rect.centerx, rect.centery - 100 + shift_y))
            self.screen.blit(text_img, text_rect)
            shift_y += self.font.get_height()

    def draw_back_screen_overlay(self, screen_size: tuple) -> None:
        overlay = pygame.Surface((screen_size[0], screen_size[1]))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(180)
        self.screen.blit(overlay, (0, 0))
