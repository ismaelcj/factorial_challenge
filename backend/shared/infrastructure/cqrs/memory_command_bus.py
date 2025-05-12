from typing import Type

from backend.shared.domain.cqrs.command import Command
from backend.shared.domain.cqrs.command_bus import CommandBus
from backend.shared.domain.cqrs.command_handler import CommandHandler


class MemoryCommandBus(CommandBus):
    def __init__(self) -> None:
        self._handlers: dict = {}

    def register(self, command: Type[Command], handler: CommandHandler) -> None:
        self._handlers[command] = handler

    def dispatch(self, command: Command) -> None:
        if type(command) not in self._handlers:
            raise Exception(f"No handler registered for command: {type(command)}")
        handler = self._handlers[type(command)]
        handler.handle(command)
