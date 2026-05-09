import pygame

from screens.const.screen_constants import LOGOUT_SCREEN, CHARACTER_SCREEN
from screens.popup.default_popup import DefaultPopupScreen
from screens.popup.popup_factory import PopupFactory


@PopupFactory.register("dead")
class DeathPopupScreen(DefaultPopupScreen):
    _BOX_CHARS = {
        "tl": "+", "tr": "+", "bl": "+", "br": "+",
        "h": "-", "v": "|",
    }

    def __init__(
            self,
            screen: pygame.Surface,
            font: pygame.font.Font,
    ):
        self.screen = screen
        self.font = font
        self.title = "  You are dead "
        self.buttons = [
            ("Logout", LOGOUT_SCREEN),
            ("Character Screen", CHARACTER_SCREEN),
        ]
        self.padding = 24
        self.line_height = 36

        self._selected = 0
        self._width = 400

        rows = 1 + 1 + len(self.buttons)
        self._height = self.padding * 2 + rows * self.line_height

        sw, sh = screen.get_size()
        self._x = (sw - self._width) // 2
        self._y = (sh - self._height) // 2

    def handle_event(self, event: pygame.event.Event) -> str | None:
        if event.type != pygame.KEYDOWN:
            return None

        if event.key in (pygame.K_UP, pygame.K_w):
            self._selected = (self._selected - 1) % len(self.buttons)

        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self._selected = (self._selected + 1) % len(self.buttons)

        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
            _, action_key = self.buttons[self._selected]
            return action_key

        return None

    def draw(self):
        ch = self._box_chars
        cw, _ = self.font.size("═")
        cols = self._width // cw

        surface = pygame.Surface((self._width, self._height))
        surface.fill((0, 0, 0))

        y = 0

        top = ch["tl"] + ch["h"] * (cols - 2) + ch["tr"]
        self._render_line(surface, top, y, (180, 180, 180))
        y += self.line_height

        self._render_line(surface, self._frame_text(self.title, cols), y, (255, 80, 80))
        y += self.line_height

        sep = ch["v"] + ch["h"] * (cols - 2) + ch["v"]
        self._render_line(surface, sep, y, (180, 180, 180))
        y += self.line_height

        for i, (label, _) in enumerate(self.buttons):
            is_selected = (i == self._selected)
            if is_selected:
                display = self._frame_text(f"► {label}", cols)
                color = (255, 255, 0)
            else:
                display = self._frame_text(f"  {label}", cols)
                color = (200, 200, 200)
            self._render_line(surface, display, y, color)
            y += self.line_height

        bot = ch["bl"] + ch["h"] * (cols - 2) + ch["br"]
        self._render_line(surface, bot, y, (180, 180, 180))

        self.screen.blit(surface, (self._x, self._y))

    @property
    def _box_chars(self):
        return self._BOX_CHARS

    def _render_line(self, surface: pygame.Surface, text: str, y: int, color: tuple):
        img = self.font.render(text, True, color)
        surface.blit(img, (0, y))

    def _frame_text(self, text: str, cols: int) -> str:
        inner = cols - 2
        centered = text.center(inner)[:inner]
        return self._BOX_CHARS["v"] + centered + self._BOX_CHARS["v"]