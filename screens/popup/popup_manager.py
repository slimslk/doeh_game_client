from screens.popup.default_popup import DefaultPopupScreen


class PopupManager:
    def __init__(self):
        self.stack: list[DefaultPopupScreen] = []

    def open(self, popup):
        self.stack.append(popup)

    def close(self):
        if self.stack:
            self.stack.pop()

    def close_all(self):
        self.stack.clear()

    def current(self):
        if self.stack:
            return self.stack[-1]
        return None

    def draw(self):
        if not self.stack:
            return
        self.current().draw()

    def handle_event(self, event):
        if self.current():
            return self.current().handle_event(event)

    def is_active(self):
        return len(self.stack) > 0
