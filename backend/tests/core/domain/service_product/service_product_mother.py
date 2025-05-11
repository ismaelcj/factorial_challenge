from backend.core.domain.category import Category
from backend.core.domain.service_product.service_product import ServiceProduct
from backend.shared.domain.value_objects.custom_uuid import Uuid


class ServiceProductMother:
    @staticmethod
    def create(
        product_id: str = Uuid.generate().value,
        name: str = "Test Service",
        category: Category = Category.FRAME_FINISH,
    ) -> ServiceProduct:
        return ServiceProduct.create(product_id, name, category)
