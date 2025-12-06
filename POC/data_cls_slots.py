from dataclasses import dataclass

@dataclass
class ProductNoSlots:
    id: int
    name: str
    price: float


p = ProductNoSlots(1, "Laptop", 50000)
print(p.__dict__)   # visible and modifiable
p.new_field = "extra"  # allowed
