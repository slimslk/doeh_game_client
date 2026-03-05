import httpx
import pygame

from connector.server_connector import ServerConnector
from core.context import AppContext
from core.game_map import GameMap
from core.game_service import GameService
from core.player import Player
from core.screen_flow import ScreenFlow
from screens.character_select_screen import CharacterSelectScreen
from screens.connecting_screen import ConnectingScreen
from screens.game_screen import GameScreen

from screens.login_screen import LoginScreen
from screens.logout_screen import LogoutScreen
from screens.register_screen import RegisterScreen
from screens.start_screen import StartScreen

running = True

client = httpx.Client(timeout=10.0, trust_env=False)

pygame.init()
screen = pygame.display.set_mode((1200, 800))
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

context = AppContext()
connector = ServerConnector(client, context)
context.connector = connector

player = Player()
game_map = GameMap()

game_service = GameService(screen, font, player, game_map)
context.game_service = game_service

flow = ScreenFlow(screen, font)
flow.set_context(context)

flow.register("start", lambda s, f, c: StartScreen(s, f, c))
flow.register("login", lambda s, f, c: LoginScreen(s, f, c))
flow.register("register", lambda s, f, c: RegisterScreen(s, f, c))
flow.register("login_success", lambda s, f, c: CharacterSelectScreen(s, f, c))
flow.register("connect", lambda s, f, c: ConnectingScreen(s, f, c))
flow.register("game", lambda s, f, c: GameScreen(s, f, c, player, game_map))
flow.register("logout", lambda s, f, c: LoginScreen(s, f, c))
flow.register("logout", lambda s, f, c: LogoutScreen(s, f, c))

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
