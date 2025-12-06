from collections import namedtuple
from dataclasses import dataclass

@dataclass(frozen=True)
class Stock:
    symbol: str
    price: float
    volume: int

    def display(self):
        return f"Stock(symbol={self.symbol}, price={self.price}, volume={self.volume})"

    def modify_price(self, new_price: float):
        self.newPrice = new_price
        return self.newPrice  # dataclasses.FrozenInstanceError: cannot assign to field 'newPrice'
        #return Stock(self.symbol, new_price, self.volume)
    
stock = Stock("AAPL", 150.0, 1000)
print(stock.symbol)
print(stock.display())
stock = Stock("GOOGL", 150.0, 1000)
print(stock.price)
print(stock.display())
print(stock.modify_price(155.0).display()) 
stock.price=200.0  # # dataclasses.FrozenInstanceError: cannot assign to field 'price'
