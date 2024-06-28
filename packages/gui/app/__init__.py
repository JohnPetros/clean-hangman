from flet import app, AppView

from gui.app.types import UI
from gui.app.screens import init_screens
from gui.app.constants.directories import DIRECTORIES


def init_app():
    def init_ui(ui: UI):
        init_screens(ui)

    app(target=init_ui, assets_dir=DIRECTORIES.assets, view=AppView.WEB_BROWSER, port=46857)
