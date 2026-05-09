class AppContext:
    def __init__(self):
        self.token: str | None = None
        self.user = None
        self.characters = []
        self.selected_character = None
        self.ws = None
        self.connector = None
        self.game_service = None
        self.data = None
        self.popup_manager = None
