from backend.core.domain.category import Category
from backend.core.domain.customizable_product.product_option import ProductOption
from backend.core.domain.customizable_product.product_option_value import ProductOptionValue
from backend.shared.domain.value_objects.custom_uuid import Uuid


class CustomizableProductConfiguration:
    def __init__(self, config_id: Uuid, options: list[ProductOption]):
        self._id = config_id
        self._options = options

    def add_option(self, name: str, category: Category, required: bool = False) -> None:
        assert not self._is_category_already_in_options(category),\
            "Category already exists in this configuration"
        option = ProductOption.create(
            option_id=Uuid.generate().value,
            name=name,
            category=category.value,
            required=required
        )
        self._options.append(option)

    @property
    def options(self) -> list[ProductOption]:
        return self._options

    def _is_category_already_in_options(self, category: Category) -> bool:
        return any(option.category == category for option in self._options)

    def are_option_values_valid(self, selected_values: list[ProductOptionValue]) -> bool:
        required_options = [option for option in self._options if option.is_required]
        selected_option_ids = [value.option_id for value in selected_values]
        
        for required_option in required_options:
            if required_option.id not in selected_option_ids:
                return False
                
        return True
