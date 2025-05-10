import uuid

from core.domain.service_product.service_product import ServiceProduct

class ServiceProductMother:
    @staticmethod
    def create(
        product_id: str = uuid.uuid4().hex,
        name: str = "Test Service"
    ) -> ServiceProduct:
        return ServiceProduct.create(product_id, name)
