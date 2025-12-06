from collections import namedtuple 


"""
auto __init__ , immutable , performance : fastest , validaton : No, Best for : lightweight data 
"""

Point = namedtuple("stock", ["symbol", "price", "volume"])
p1 = Point("AAPL", 150.0, 1000)
print(p1.symbol)
p2 = Point("GOOGL", 2800.5, 500)
print(p2.price)