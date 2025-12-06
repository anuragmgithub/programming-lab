from dataclasses import dataclass

@dataclass
class ProductNoSlots:
    id: int
    name: str
    price: float

@dataclass(slots=True)
class ProductSlots:
    id: int
    name: str
    price: float


p = ProductNoSlots(1, "Laptop", 50000)
print(p.__dict__)   # visible and modifiable ,Every normal Python object stores its attributes in a dictionary called __dict__.
p.new_field = "extra"  # allowed

ps = ProductSlots(2, "Mobile", 25000)
print(ps.__dict__)  # AttributeError: 'ProductSlots' object has no attribute '__dict__'
# ps.new_field = "extra"  # AttributeError: 'ProductSlots ' object has no attribute 'new_field'
