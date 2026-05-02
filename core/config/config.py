import json

CONFIG_FILE_NAME = "config.json"


def calculate_game_field_size(sr_w, sr_h, gf_font):
    width = int(sr_w / gf_font) - 10
    width = 71 if width > 71 else width
    height = int(sr_h / gf_font) - 10
    height = 39 if height > 39 else height
    return width, height


with open(CONFIG_FILE_NAME, "r") as config:
    config = json.load(config)

server_url = config["server_url"]
ws_url = config["ws_url"]
display_settings = config["display_settings"]

screen_resolution_width = display_settings.get("screen_resolution_width")
screen_resolution_height = display_settings.get("screen_resolution_height")
screen_font_size = display_settings.get("screen_font_size")

game_field_font_size = display_settings.get("game_field_font_size")
game_field_width, game_field_height = calculate_game_field_size(screen_resolution_width,
                                                                screen_resolution_height,
                                                                game_field_font_size)

key_mapping = config["key_mapping"]
max_messages = config.get("max_messages", 100)
