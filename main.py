import httpx
import pygame

from connector.server_connector import ServerConnector
from core.context import AppContext
from core.screen_flow import ScreenFlow

from screens.login_screen import LoginScreen
from screens.character_select_screen import CharacterSelectScreen
from screens.register_screen import RegisterScreen
from screens.start_screen import StartScreen

running = True

client = httpx.Client(timeout=10.0, trust_env=False)
connector = ServerConnector(client)

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

context = AppContext()
context.connector = connector

flow = ScreenFlow(screen, font)
flow.set_context(context)

flow.register("start", lambda s, f, c: StartScreen(s, f, c))
flow.register("login", lambda s, f, c: LoginScreen(s, f, c))
flow.register("login_success", lambda s, f, c: CharacterSelectScreen(s, f, c))
flow.register("register", lambda s, f, c: RegisterScreen(s, f, c))
flow.register("logout", lambda s, f, c: LoginScreen(s, f, c))

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
