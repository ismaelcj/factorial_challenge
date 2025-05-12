from abc import ABC, abstractmethod
from typing import Type

from backend.shared.domain.cqrs.command import Command
from backend.shared.domain.cqrs.command_handler import CommandHandler


class CommandBus(ABC):
    @abstractmethod
    def register(self, command: Type[Command], handler: CommandHandler) -> None:
        pass

    @abstractmethod
    def dispatch(self, command: Command) -> None:
        pass
