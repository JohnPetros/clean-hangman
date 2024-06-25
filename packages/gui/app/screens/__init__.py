from gui.app.types import UI

from .home.home_view import home_view


def init_screens(ui: UI):
    home_view(ui)
