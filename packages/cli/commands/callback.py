from typer import Option


from cli.views import version_view


def callback(
    should_show: bool = Option(
        False,
        "--version",
        "-v",
        help="Version number",
        callback=version_view,
        is_eager=True,
        is_flag=True,
    ),
):
    if should_show:
        print("Laura Gabriel")
