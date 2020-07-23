# stock.py

class Stock:
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name:str, shares:int, price:float):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    def sell(self, amount):
        if amount <= self.shares:
            self.shares -= amount