import json

CONFIG_FILE_NAME = "config.json"


def calculate_game_field_size(sr_w: int, sr_h: int, gf_font: int):
    width = sr_w // gf_font - gf_font
    width = 49 if width > 49 else width
    height = sr_h // gf_font - gf_font
    height = 25 if height > 25 else height
    return width, height


def calculate_screen_resolution(sr_w: int, sr_h: int, s_font_size: int):
    w, h = (sr_w // s_font_size) * s_font_size, (sr_h // s_font_size) * s_font_size
    return w, h


with open(CONFIG_FILE_NAME, "r") as config:
    config = json.load(config)

server_url = config["server_url"]
ws_url = config["ws_url"]
display_settings = config["display_settings"]

screen_font_size = int(display_settings.get("screen_font_size"))
screen_resolution_width, screen_resolution_height = (
    calculate_screen_resolution(int(display_settings.get("screen_resolution_width")),
                                int(display_settings.get("screen_resolution_height")),
                                screen_font_size))
game_field_font_size = int(display_settings.get("game_field_font_size"))
game_field_width, game_field_height = calculate_game_field_size(screen_resolution_width,
                                                                screen_resolution_height,
                                                                game_field_font_size)

key_mapping = config["key_mapping"]
max_messages = config.get("max_messages", 100)
