from flet import app, AppView

from gui.app.types import UI
from gui.app.screens import init_screens


def init_app():
    def init_ui(ui: UI):
        init_screens(ui)

    app(target=init_ui)
