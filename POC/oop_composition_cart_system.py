class Product:
    def __init__(self, id:int, name:str, price:float, category:str):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    
    def is_category(self, category:str) -> bool:
        return self.category.lower() == category.lower()

class Cart:
    def __init__(self):
        self.products: list[Product] = []
    
    def add_product(self, Product:Product):
        self.products.append(Product)
        print(f"Product '{Product.name}' added to cart.")
    
    def remove_product(self, product_id: int):
        self.products = [p for p in self.products if p.id != product_id]
        print(f"Product ID {product_id} removed from cart.")

    def search_by_category(self, category_name: str) -> list[Product]:
        return [p for p in self.products if p.is_category(category_name)]

    def total_price(self) -> float:
        return sum(p.price for p in self.products)


cart = Cart()

cart.add_product(Product(1, "Laptop", 50000, "Electronics"))
cart.add_product(Product(2, "Shoes", 3000, "Fashion"))
cart.add_product(Product(3, "Mobile", 25000, "Electronics"))

electronics = cart.search_by_category("Electronics")
print([p.name for p in electronics]) 

print(cart.total_price()) 

