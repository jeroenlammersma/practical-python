# stock.py
from . import typedproperty as tp

def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

class Stock:
    __slots__ = ('_name', '_shares', '_price')
    name = tp.String('name')
    shares = tp.Integer('shares')
    price = tp.Float('price')

    def __init__(self, name:str, shares:int, price:float):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
            
    @logged
    def sell(self, amount):
        if amount <= self.shares:
            self.shares -= amount