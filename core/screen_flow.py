class ScreenFlow:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

        self.context = None
        self.current_screen = None

        self.routes = {}

    def set_context(self, context):
        self.context = context

    def register(self, event_name, screen_factory):
        self.routes[event_name] = screen_factory

    def start(self, start_event="start"):
        self.transition(start_event)

    def transition(self, event, data=None):
        if self.current_screen:
            self.current_screen.on_exit()

        if data:
            for key, value in data.items():
                setattr(self.context, key, value)

        if event not in self.routes:
            raise ValueError(f"No route for event '{event}'")

        self.current_screen = self.routes[event](
            self.screen,
            self.font,
            self.context
        )

        self.current_screen.on_enter()

    def handle_event(self, event):
        result = self.current_screen.handle_event(event)
        if result:
            self.transition(
                result["event"],
                result.get("data")
            )

    def draw(self):
        self.current_screen.draw()
