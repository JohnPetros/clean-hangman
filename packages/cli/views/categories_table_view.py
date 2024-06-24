from time import sleep

from rich.table import Table

from core.constants import CATEGORIES_EMOJIS

from cli.utils import console


def categories_table_view():
    categories_table = Table(
        "Pick one of the following categories:", expand=True, leading=1
    )

    with console.status("Loading...", spinner="material"):
        sleep(2)

    categories_table.add_row(
        f"(P) Programming {CATEGORIES_EMOJIS.programming}\t  (A) Animals {CATEGORIES_EMOJIS.animals}"
    )
    categories_table.add_row(
        f"(C) Countries {CATEGORIES_EMOJIS.countries}\t\t(F) Fruits {CATEGORIES_EMOJIS.fruits}"
    )
    categories_table.add_row(
        f"(S) Sports {CATEGORIES_EMOJIS.sports}\t\t(O) Objects {CATEGORIES_EMOJIS.objects}"
    )

    console.print(categories_table)
