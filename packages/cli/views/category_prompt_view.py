from cli.utils import prompt, console

from core.constants import CATEGORIES_WORDS

from cli.constants import CATEGORIES_EMOJIS


def category_prompt_view():
    categories = CATEGORIES_WORDS._fields
    letters = [category[0] for category in categories]

    letter = ""

    while True:
        letter = prompt.ask("[blue]Category letter[/blue]").strip().lower()

        if letter not in letters:
            console.print("[red b]Invalid letter 😡[/red b]")
        else:
            break

    filtered_categories = filter(lambda category: category[0] == letter, categories)
    category_name = list(filtered_categories)[0]
    category_emoji = getattr(CATEGORIES_EMOJIS, category_name)

    return category_name, category_emoji
