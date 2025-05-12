from backend.core.domain.product_compatibility.product_incompatibility import ProductIncompatibility
from backend.shared.domain.value_objects.custom_uuid import Uuid


class ProductIncompatibilityMother:
    
    @staticmethod
    def create(product_a_id=None, product_b_id=None, reason="Default incompatibility reason"):
        product_a_id = product_a_id or Uuid.generate()
        product_b_id = product_b_id or Uuid.generate()
        
        return ProductIncompatibility(
            Uuid.generate(),
            product_a_id if isinstance(product_a_id, Uuid) else Uuid(product_a_id),
            product_b_id if isinstance(product_b_id, Uuid) else Uuid(product_b_id),
            reason
        )
    
    @staticmethod
    def create_for_products(product_a_id, product_b_id, reason="Products are incompatible"):
        return ProductIncompatibilityMother.create(product_a_id, product_b_id, reason)
