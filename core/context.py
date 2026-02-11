class AppContext:
    def __init__(self):
        self.token: str = None
        self.user = None
        self.characters = []
        self.selected_character = None
        self.connector = None
