from abc import ABC, abstractmethod
from typing import Generic

from backend.shared.domain.cqrs.command import CommandType


class CommandHandler(Generic[CommandType], ABC):

    @abstractmethod
    def handle(self, command: CommandType) -> None:
        pass
