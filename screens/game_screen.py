import pygame

from core import controller
from core.context import AppContext
from core.game_map import GameMap
from screens.base_screen import BaseScreen
from core.config.config import game_field_width, game_field_height, key_mapping, game_field_font_size


class GameScreen(BaseScreen):
    _UI_OFFSET = 5

    def __init__(self, screen, font, context: AppContext, player, game_map: GameMap):
        super().__init__(screen, font, context)
        self.context = context
        self.player = player
        self.game_map = game_map

        self.game_field_font_size = game_field_font_size

        self.display_map_width = game_field_width
        self.display_map_height = game_field_height
        self.player_coord = (self.display_map_width // 2, self.display_map_height // 2)
        self.actions = key_mapping
        self.is_created = False

        self.player.name = self.context.selected_character

    def handle_event(self, event):
        action = controller.handle_event(event)
        if action == "exit":
            return {"event": "logout"}
        if self.player.is_dead:
            return {"event": "logout"}  # TODO Add dead screen instead logout
        if action and isinstance(action, dict):
            self.context.ws.send(action)

    def draw(self):
        self.screen.fill((0, 0, 0))
        px, py = self.player.position

        # --- 1. Top status line ---
        top_text = f"Player: {self.player.name} || Inventory: {'|'.join(self.player.inventory)}"
        top_surface = self.font.render(top_text, True, (255, 255, 255))
        self.screen.blit(top_surface, (0, 0))

        # --- 2. Camera & Map Boundary Logic ---
        map_w, map_h = self.game_map.get_map_size()
        ui_height_offset = top_surface.get_height() + self._UI_OFFSET

        # Define cell dimensions once
        padding = 2
        cell_w = self.game_field_font_size + padding
        cell_h = self.game_field_font_size + padding

        # Logic for Horizontal (X)
        if map_w <= self.display_map_height:
            cam_x = 0
            render_w = map_w
            screen_offset_x = (self.display_map_height - map_w) * cell_w // 2
        else:
            # Standard centering logic: Player minus half-screen
            cam_x = px - (self.display_map_height // 2)
            # Clamp to bounds [0, map_w - display_w]
            cam_x = max(0, min(cam_x, map_w - self.display_map_height))
            render_w = self.display_map_height
            screen_offset_x = 0

        # Logic for Vertical (Y)
        if map_h <= self.display_map_width:
            cam_y = 0
            render_h = map_h
            screen_offset_y = 0
        else:
            cam_y = py - (self.display_map_width // 2)
            cam_y = max(0, min(cam_y, map_h - self.display_map_width))
            render_h = self.display_map_width
            screen_offset_y = 0

        # --- 3. Rendering Grid ---
        grid = self.game_map.get_map()

        for s_x in range(render_w):
            for s_y in range(render_h):
                # Map coordinates
                m_x = cam_x + s_x
                m_y = cam_y + s_y

                # Bounds safety check
                if 0 <= m_x < map_w and 0 <= m_y < map_h:
                    try:
                        # Access map data (using grid[x][y] as per your previous shift)
                        char, color = grid[m_x][m_y]

                        # # Check for player
                        # if m_x == px and m_y == py:
                        #     char, color = "@", (255, 255, 0)

                        img = self.font.render(char, True, color)

                        # Calculate exact screen position
                        draw_x = ui_height_offset + screen_offset_x + (s_x * cell_w)
                        draw_y = ui_height_offset + screen_offset_y + (s_y * cell_h)
                        self.screen.blit(img, (draw_y, draw_x))
                    except IndexError:
                        continue

        # --- 4. Bottom stats line ---
        stats_text = (f"HP: {self.player.health}"
                      f" ST: {self.player.energy}"
                      f" SAT: {self.player.hungry}"
                      f" AM: {self.player.attack_modifier}"
                      f" AD: {self.player.attack_damage}"
                      f" DEF: {self.player.defence}")
        stats_surface = self.font.render(stats_text, True, (255, 255, 0))
        self.screen.blit(stats_surface, (0, top_surface.get_height() + self._UI_OFFSET * 2 +
                                         self.display_map_height * (self.game_field_font_size + padding)))
        message_test = f"{self.player.messages[-1]}"
        message_surface = self.font.render(message_test, True, (255, 255, 0))
        self.screen.blit(message_surface, (0, top_surface.get_height() + self._UI_OFFSET * 2 +
                                           self.display_map_height * (self.game_field_font_size + padding) +
                                           stats_surface.get_height()))

        pygame.display.flip()

    def update_size(self, height, width):
        self.display_map_height = height
        self.display_map_width = width
