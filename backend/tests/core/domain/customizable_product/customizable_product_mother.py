from backend.core.domain.category import Category
from backend.core.domain.customizable_product.customizable_product import CustomizableProduct
from backend.shared.domain.value_objects.custom_uuid import Uuid


class CustomizableProductMother:
    @staticmethod
    def create(
        product_id: str = Uuid.generate().value,
        name: str = "Custom Bicycle",
        category: str = Category.BICYCLE.value,
    ) -> CustomizableProduct:
        return CustomizableProduct.create(
            product_id=product_id,
            name=name,
            category=category,
        )

    @staticmethod
    def create_with_options(
        product_id: str = Uuid.generate().value,
        name: str = "Custom Bicycle",
        category: str = Category.BICYCLE.value,
    ) -> CustomizableProduct:
        product = CustomizableProductMother.create(product_id, name, category)
        product.add_option("Frame", Category.FRAME, required=True)
        product.add_option("Finish", Category.FRAME_FINISH, required=False)
        return product
