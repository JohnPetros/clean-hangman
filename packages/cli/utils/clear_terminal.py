from os import system
from platform import system as system_name


def clear_terminal():
    system("cls" if system_name() == "Windows" else "clear")
