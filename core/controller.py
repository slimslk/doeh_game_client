import pygame
from core.config.config import key_mapping

keys = key_mapping


def handle_event(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return {"action": "exit"}
        action = keys.get(event.unicode, None)
        return action
