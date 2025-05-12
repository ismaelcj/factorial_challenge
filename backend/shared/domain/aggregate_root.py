from abc import ABC

from backend.shared.domain.value_objects.custom_uuid import Uuid


class AggregateRoot(ABC):
    def __init__(self, aggregate_id: Uuid) -> None:
        self._id = aggregate_id

    @property
    def id(self) -> Uuid:
        return self._id
