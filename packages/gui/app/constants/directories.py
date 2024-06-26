from collections import namedtuple
from pathlib import Path

directories_tuple = namedtuple("DIRECTORIES", ["assets"])

path = Path(__file__).parent.parent.parent.parent

DIRECTORIES = directories_tuple(str(path.absolute() / "gui" / "assets"))
