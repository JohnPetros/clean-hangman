from typer import Exit
from rich.padding import Padding

from cli.utils import console
from cli.constants import VERSION


def version_view(should_show: bool):
    if should_show:
        console.print(Padding(f"Version: [yellow on red]{VERSION}[/]", pad=(0, 4)))
        raise Exit(code=0)
