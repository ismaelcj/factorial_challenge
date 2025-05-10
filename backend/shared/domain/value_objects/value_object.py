from abc import ABC, abstractmethod
from typing import Any


class ValueObject(ABC):
    @property
    @abstractmethod
    def value(self) -> Any:
        pass

    def __str__(self) -> str:
        pass
