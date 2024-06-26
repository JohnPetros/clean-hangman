from core.structs import Game, Category

from cli.views import (
    title_view,
    categories_table_view,
    category_prompt_view,
    end_game_view,
    reset_game_view,
    exit_game_view,
    hangman_view,
    blanks_group_view,
    keyboard_view,
    keyboard_letter_prompt,
)
from cli.utils import console, clear_terminal


def start_command():
    should_exit = False

    while not should_exit:
        title_view()
        categories_table_view()
        category_name, category_emoji = category_prompt_view()

        category = Category(category_name)
        game = Game.create(category)

        is_end_game = False
        is_win = False
        should_reset = False

        while not should_reset:
            clear_terminal()

            title_view()

            hangman_view(game.attempts_count.value)

            blanks_group_view(
                category=f"{category_name} {category_emoji}",
                blanks=game.blanks_group.value,
            )

            keyboard_view(
                correct_letters=list(game.correct_word.value),
                used_letters=game.used_letters,
            )

            while True:
                try:
                    letter = keyboard_letter_prompt(is_end_game)

                    if letter == "reset":
                        clear_terminal()
                        should_reset = True
                        break

                    if letter == "exit":
                        should_reset = True
                        should_exit = True
                        break

                    game = game.input_letter(letter)

                    if game.check_win():
                        is_win = True
                        is_end_game = True
                    elif game.check_lose():
                        is_win = False
                        is_end_game = True

                    if not is_end_game:
                        break
                    else:
                        clear_terminal()
                        end_game_view(is_win, game.correct_word.value)
                        reset_game_view()
                except ValueError as error:
                    console.print(f"[red b]{error}[/]")

    clear_terminal()
    exit_game_view()
