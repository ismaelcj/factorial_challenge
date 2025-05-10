import uuid

from backend.shared.domain.value_objects.value_object import ValueObject


class Uuid(ValueObject):
    def __init__(self, value: str) -> None:
        self.ensure_valid_uuid(value)
        self._value = value

    @classmethod
    def generate(cls) -> 'Uuid':
        return Uuid(uuid.uuid4().hex)

    @staticmethod
    def ensure_valid_uuid(value: str) -> None:
        try:
            uuid.UUID(value)
        except ValueError:
            raise ValueError(f"Invalid UUID: {value}")

    @property
    def value(self) -> str:
        return self._value
