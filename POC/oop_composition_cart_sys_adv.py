from dataclasses import dataclass, field
from typing import Optional, Union

@dataclass
class Product:
    id: int
    name: str
    price: float
    category: str

    def is_category(self, category: str) -> bool:
        return self.category.lower() == category.lower()


@dataclass
class Cart:
    products: list[Product] = field(default_factory=list)

    def add_product(self, product: Product):
        self.products.append(product)
        print(f"Product '{product.name}' added to cart.")

    def remove_product(self, product_id: int):
        self.products = [p for p in self.products if p.id != product_id]
        print(f"Product ID {product_id} removed from cart.")

    def search_by_category(self, category_name: str) -> list[Product]:
        return [p for p in self.products if p.is_category(category_name)]

    def total_price(self) -> float:
        return sum(p.price for p in self.products)

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def discounted_total(self, discount: Union[float, int]) -> float:
        total = self.total_price()
        if isinstance(discount, float) and 0 < discount < 1:
            return total * (1 - discount)
        elif isinstance(discount, int) and 0 < discount < total:
            return total - discount
        else:
            print("Invalid discount value.")
            return total


cart = Cart()
cart.add_product(Product(1, "Laptop", 50000, "Electronics"))
cart.add_product(Product(2, "Shoes", 3000, "Fashion"))
cart.add_product(Product(3, "Mobile", 25000, "Electronics"))
electronics = cart.search_by_category("Electronics")
print([p.name for p in electronics])  
print(cart.total_price()) 
