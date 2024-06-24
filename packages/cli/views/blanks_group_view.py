from rich.align import Align

from cli.utils import console


def blanks_group_view(category: str, blanks: list[str]):
    console.print((Align(f"[u]Category[/u]: [blue b]{category}[/]", "center")))

    console.print("\n")

    blanks = "  ".join([blank.upper() for blank in blanks])

    console.print(Align(f"[b]{blanks}[/b]", align="center"), end=" ")
