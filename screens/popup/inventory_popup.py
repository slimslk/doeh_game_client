import pygame

from screens.popup.popup_factory import PopupFactory


@PopupFactory.register('inventory')
class InventoryPopupScreen:
    def __init__(
            self,
            screen: pygame.Surface,
            font: pygame.font.Font,
            inventory: list[str],
            text_color: tuple[int, int, int] = (255, 255, 255),
    ):
        self.screen = screen
        self.font = font
        self.inventory = inventory
        self.text_color = text_color
        self._selected = 0
        self._min_width = 25 * self.font.size("=")[0]
        self._min_height = 15 * self.font.size("=")[1]
        self.page_size = self._min_height // self.font.get_height() - 4

        print(self.screen.get_size(), self._min_width // 2, self._min_height // 2)
        self.rect = pygame.Rect(
            (self.screen.get_size()[0] // 2) - (self._min_width // 2),
            (self.screen.get_size()[1] // 2) - (self._min_height // 2),
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

        elif event.key == pygame.K_ESCAPE:
            return "return"

        return None

    def draw(self):
        screen_size = self.screen.get_size()
        self.draw_back_screen_overlay(screen_size)
        rect = pygame.draw.rect(self.screen, (0, 0, 0), self.rect)

        start = max(0, self._selected - self.page_size + 1)
        end = start + self.page_size

        # --- Title ---
        title_text = "Inventory"
        title = self.font.render(title_text, True, self.text_color)
        title_rect = title.get_rect(
            centerx=self.rect.centerx,
            top=self.rect.top,
        )
        self.screen.blit(title, title_rect)
        title_text = "=" * 25
        title = self.font.render(title_text, True, self.text_color)
        title_rect = title.get_rect(
            centerx=self.rect.centerx,
            top=title_rect.bottom,
        )
        self.screen.blit(title, title_rect)

        # --- Inventory ---
        shift_y = title_rect.bottom
        for index, item in enumerate(self.inventory[start:end]):
            if start + index == self._selected:
                text_img = self.font.render(f">  {item}  <", True, (255, 255, 255))
            else:
                text_img = self.font.render(f"{item}", True, (255, 255, 255))
            text_rect = text_img.get_rect(centerx=self.rect.centerx, top=shift_y)
            self.screen.blit(text_img, text_rect)
            shift_y += self.font.get_height()

        # --- Bottom text ---
        bottom_text = "=" * 25
        bottom = self.font.render(bottom_text, True, self.text_color)
        bottom_rect = title.get_rect(
            centerx=self.rect.centerx,
            top=text_rect.bottom,
        )
        self.screen.blit(bottom, bottom_rect)

    def draw_back_screen_overlay(self, screen_size: tuple) -> None:
        overlay = pygame.Surface((screen_size[0], screen_size[1]))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(180)
        self.screen.blit(overlay, (0, 0))
