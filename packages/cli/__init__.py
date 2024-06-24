from typer import Typer

from cli.commands import init_commands


def init_cli():
    app = Typer()

    init_commands(app)

    app()
