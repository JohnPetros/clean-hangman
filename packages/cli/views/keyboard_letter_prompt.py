from rich.text import Text


from cli.utils import prompt, console


def keyboard_letter_prompt(is_end_game: bool):
    console.print("\n")

    prompt_text = Text(
        (
            "Type an avaliable letter from the keyboard (in white)"
            if not is_end_game
            else "Or type 'exit' to exit"
        ),
        style="blue b",
    )

    response = prompt.ask(prompt_text).strip().lower()

    return response
