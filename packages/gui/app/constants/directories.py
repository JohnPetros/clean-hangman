from collections import namedtuple
from pathlib import Path

directories_tuple = namedtuple("DIRECTORIES", ["assets"])

path = Path()

DIRECTORIES = directories_tuple(str(path.absolute() / "gui" / "assets"))
