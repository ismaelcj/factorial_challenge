from abc import ABC

from backend.shared.domain.value_objects.custom_uuid import Uuid


class Entity(ABC):
    def __init__(self, entity_id: Uuid):
        self._id = entity_id

    @property
    def id(self) -> Uuid:
        return self._id

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
