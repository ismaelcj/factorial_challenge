from abc import ABC
from typing import TypeVar


class Command(ABC):
    pass

CommandType = TypeVar('CommandType', bound=Command)