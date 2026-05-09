import httpx
import pygame

from connector.server_connector import ServerConnector
from core.context import AppContext
from core.game_map import GameMap
from core.game_service import GameService
from core.player import Player
from core.screen_flow import ScreenFlow
from core.config.config import screen_font_size
from screens.character_select_screen import CharacterSelectScreen
from screens.connecting_screen import ConnectingScreen
from screens.game_screen import GameScreen

from screens.login_screen import LoginScreen
from screens.logout_screen import LogoutScreen
from screens.popup.popup_manager import PopupManager
from screens.register_screen import RegisterScreen
from screens.start_screen import StartScreen

from core.config.config import screen_resolution_width, screen_resolution_height
import screens.const.screen_constants as s_const
from screens.popup import death_screen_popup, exit_game_popup, inventory_popup

running = True

client = httpx.Client(timeout=10.0, trust_env=False)

pygame.init()
screen = pygame.display.set_mode((screen_resolution_width, screen_resolution_height))
font = pygame.font.Font("fonts/JetBrainsMono-Bold.ttf", screen_font_size)
clock = pygame.time.Clock()

context = AppContext()
connector = ServerConnector(client, context)
context.connector = connector

player = Player()
game_map = GameMap()
popup_manager = PopupManager()

game_service = GameService(screen, font, player, game_map)
context.game_service = game_service
context.popup_manager = popup_manager

flow = ScreenFlow(screen, font)
flow.set_context(context)

flow.register(s_const.START_SCREEN, lambda s, f, c: StartScreen(s, f, c))
flow.register(s_const.LOGIN_SCREEN, lambda s, f, c: LoginScreen(s, f, c))
flow.register(s_const.REGISTER_SCREEN, lambda s, f, c: RegisterScreen(s, f, c))
flow.register(s_const.CHARACTER_SCREEN, lambda s, f, c: CharacterSelectScreen(s, f, c))
flow.register(s_const.CONNECT_SCREEN, lambda s, f, c: ConnectingScreen(s, f, c))
flow.register(s_const.GAME_SCREEN, lambda s, f, c: GameScreen(s, f, c, player, game_map))
flow.register(s_const.LOGOUT_SCREEN, lambda s, f, c: LogoutScreen(s, f, c))

flow.start()


while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                flow.handle_event(event)

        flow.draw()
        clock.tick(60)
    except KeyboardInterrupt:
        connector.close()
        running = False

pygame.quit()
