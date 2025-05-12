from backend.shared.domain.value_objects.custom_uuid import Uuid
from backend.shared.domain.entity import Entity


class ProductIncompatibility(Entity):
    def __init__(self, incompatibility_id: Uuid, product_a_id: Uuid, product_b_id: Uuid, reason: str = ""):
        super().__init__(incompatibility_id)
        self._product_a_id = product_a_id
        self._product_b_id = product_b_id
        self._reason = reason

    @classmethod
    def create(cls, product_a_id: str, product_b_id: str, reason: str = "") -> 'ProductIncompatibility':
        return cls(
            Uuid.generate(),
            Uuid(product_a_id),
            Uuid(product_b_id),
            reason
        )

    @property
    def product_a_id(self) -> Uuid:
        return self._product_a_id

    @property
    def product_b_id(self) -> Uuid:
        return self._product_b_id
        
    @property
    def reason(self) -> str:
        return self._reason
        
    # def involves_product(self, product_id: Uuid) -> bool:
    #     return self._product_a_id == product_id or self._product_b_id == product_id

    def are_incompatible(self, product_id_1: Uuid, product_id_2: Uuid) -> bool:
        return ((self._product_a_id == product_id_1 and self._product_b_id == product_id_2) or
                (self._product_a_id == product_id_2 and self._product_b_id == product_id_1))
