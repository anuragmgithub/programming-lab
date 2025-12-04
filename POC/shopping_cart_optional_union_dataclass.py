from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass(slots=True)
class Product:
    """
    Represents a product item in the system.
    """
    id: int
    name: str
    price: float
    category: str

    def is_category(self, category: str) -> bool:
        """
        Checks if the product belongs to the given category.
        Case-insensitive comparison.
        """
        return self.category.lower() == category.lower()

# data class not used , however here dataclass can be used for Cart as well, howwever optional 
class Cart:
    """
    Shopping cart that can store multiple products.
    """
    #products: list[Product] = field(default_factory=list)
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """
        Adds a new product to the cart.
        """
        self.products.append(product)
        print(f"Product '{product.name}' added to cart.")

    def remove_product(self, product_id: int) -> None:
        """
        Removes a product by its ID if it exists.
        """
        before_count = len(self.products)
        self.products = [p for p in self.products if p.id != product_id]
        after_count = len(self.products)

        if before_count == after_count:
            print(f"No product found with ID: {product_id}")
        else:
            print(f"Product ID {product_id} removed from cart.")

    def search_by_category(self, category_name: str) -> list[Product]:
        """
        Returns products belonging to a particular category.
        """
        return [p for p in self.products if p.is_category(category_name)]

    def total_price(self) -> float:
        """
        Calculates the total price of all items in the cart.
        """
        return sum(p.price for p in self.products)

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """
        Returns a product object if found, otherwise None.
        """
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def discounted_total(self, discount: Union[float, int]) -> float:
        """
        Calculates total price after applying discount.
        float = percentage discount (0 < discount < 1)
        int   = flat discount amount (0 < discount < total price)
        """
        total = self.total_price()

        if isinstance(discount, float) and 0 < discount < 1:
            return total * (1 - discount)

        if isinstance(discount, int) and 0 < discount < total:
            return total - discount

        print("Invalid discount value.")
        return total


if __name__ == "__main__":
    cart = Cart()
    cart.add_product(Product(1, "Laptop", 50000, "Electronics"))
    cart.add_product(Product(2, "Shoes", 3000, "Fashion"))
    cart.add_product(Product(3, "Mobile", 25000, "Electronics"))

    electronics = cart.search_by_category("Electronics")
    print("Electronics:", [p.name for p in electronics])

    print("Total Price:", cart.total_price())
    print("Discounted Price (10%):", cart.discounted_total(0.1))
    print("Discounted Price (₹2000):", cart.discounted_total(2000))
