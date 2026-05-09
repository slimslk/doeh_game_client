from screens.popup.default_popup import DefaultPopupScreen


class PopupFactory:
    _registry = {}

    @classmethod
    def register(cls, name):
        def wrapper(popup_class):
            cls._registry[name] = popup_class
            return popup_class
        return wrapper

    @classmethod
    def create(cls, name, screen, **kwargs) -> DefaultPopupScreen:
        popup_class = cls._registry.get(name)

        if not popup_class:
            raise ValueError(f"Popup '{name}' not found")

        return popup_class(screen, **kwargs)
