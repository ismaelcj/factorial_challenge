from typing import Optional, List

from backend.core.domain.category import Category
from backend.core.domain.customizable_product.customizable_product_configuration import CustomizableProductConfiguration
from backend.core.domain.customizable_product.product_option import ProductOption
from backend.core.domain.customizable_product.product_option_value import ProductOptionValue
from backend.core.domain.pricing_context import PricingContext
from backend.core.domain.product import Product
from backend.core.domain.product_compatibility.product_incompatibility import ProductIncompatibility
from backend.core.domain.product_compatibility.product_compatibility_service import ProductCompatibilityService
from backend.shared.domain.value_objects.custom_uuid import Uuid


class CustomizableProduct(Product):
    def __init__(
        self,
        product_id: Uuid,
        name: str,
        category: Category,
        configuration: CustomizableProductConfiguration,
        selected_values: list[ProductOptionValue],
    ):
        super().__init__(product_id, name, category)
        self._configuration = configuration
        self._selected_values = selected_values

    @classmethod
    def create(cls, product_id: str, name: str, category: str) -> 'CustomizableProduct':
        new_id = Uuid(product_id)
        config = CustomizableProductConfiguration(
            config_id=new_id,
            options=[],
        )
        return cls(
            new_id,
            name,
            Category(category),
            config,
            []
        )

    def add_option(self, name: str, category: Category, required: bool = False) -> None:
        self._configuration.add_option(name, category, required)

    @property
    def options(self) -> list[ProductOption]:
        return self._configuration.options

    def add_product_option_value(self, option: ProductOption, product: Product, 
                                incompatibilities: List[ProductIncompatibility] = None) -> None:
        assert not self._is_option_already_in_selected_values(option),\
            "Option already exists in this product"

        if incompatibilities:
            selected_products = self._get_selected_products()

            validation_result = ProductCompatibilityService.validate_compatibility(
                product, selected_products, incompatibilities
            )

            assert validation_result.is_valid, validation_result.message
        
        option_value = ProductOptionValue.create(
            option_value_id=Uuid.generate().value,
            option=option,
            product=product
        )
        self._selected_values.append(option_value)

    def _is_option_already_in_selected_values(self, option: ProductOption) -> bool:
        return any(value.option_id == option.id for value in self._selected_values)

    def get_price(self, context: Optional[PricingContext] = None) -> float:
        assert self._selected_values_are_valid(), "Selected products are not valid"

        if context is None:
            context = PricingContext(
                applicable_products=self._get_selected_products()
            )

        total_price = 0
        for option in self._selected_values:
            total_price += option.get_price(context)

        return total_price

    def _selected_values_are_valid(self):
        return self._configuration.are_option_values_valid(self._selected_values)

    def _get_selected_products(self) -> List[Product]:
        return [option.product for option in self._selected_values]
