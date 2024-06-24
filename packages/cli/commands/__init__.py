from typer import Typer

from .start_command import start_command
from .callback import callback


def init_commands(app: Typer):

    app.callback(invoke_without_command=True)(callback)

    app.command(name="start", help="Start the game")(start_command)
