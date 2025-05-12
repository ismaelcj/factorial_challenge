from backend.core.domain.category import Category
from backend.shared.domain.entity import Entity
from backend.shared.domain.value_objects.custom_uuid import Uuid


class ProductOption(Entity):
    def __init__(
        self,
        option_id: Uuid,
        name: str,
        category: Category,
        required: bool,
    ):
        super().__init__(option_id)
        self._name = name
        self._category = category
        self._required = required

    @classmethod
    def create(
            cls,
            option_id: str,
            name: str,
            category: str,
            required: bool = False
    ) -> 'ProductOption':
        return cls(
            Uuid(option_id),
            name,
            Category(category),
            required
        )

    @property
    def id(self) -> Uuid:
        return self._id

    @property
    def category(self) -> Category:
        return self._category

    @property
    def is_required(self) -> bool:
        return self._required

    def __repr__(self) -> str:
        return f"ProductOption[{self._name} category={self._category.value}]"
