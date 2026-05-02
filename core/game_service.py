import pygame
import threading

from core.config.config import game_field_width, game_field_height


class GameService:
    def __init__(self, screen, font, player, game_map):
        self.screen = screen
        self.font = font
        self.state_lock = threading.Lock()

        self.player = player
        self.game_map = game_map
        self.game_map.generate_map(game_field_width,
                                   game_field_height)

        self.is_running = False

        self.clock = pygame.time.Clock()

        pygame.init()

        pygame.display.set_caption("ASCII Game Client")

        self.font.get_height()

    def apply_server_update(self, message: dict):
        with self.state_lock:
            if message.get("game_updates"):
                self.update_game_state(message["game_updates"])
            if message.get("player_stats"):
                self.update_player_stats(message["player_stats"])
            if message.get("location_updates"):
                self.update_location(message["location_updates"])

    def update_player_stats(self, player_data):
        self.player.update(player_data)

    def update_location(self, location_updates):
        self.game_map.update_map(location_updates, self.player.name)

    def update_game_state(self, game_updates: dict):
        if game_updates.get("location_size") and game_updates.get("location_data"):
            height, width = game_updates["location_size"]
            self.game_map.update_map_size(height, width)
            self.game_map.update_map(game_updates["location_data"], self.player.name)
