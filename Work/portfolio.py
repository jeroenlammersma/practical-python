# portfolio.py

from fileparse import parse_csv
from stock import Stock

class Portfolio:

    def __init__(self):
        self._holdings = []

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = parse_csv(lines,
                                select=['name', 'shares', 'price'],
                                types = [str, int, float],
                                **opts)

        for d in portdicts:
            self.append(Stock(**d))

        return self
    
    def append(self, holding):
        if not isinstance(holding, Stock):
            raise TypeError(f'Expected a Stock instance')
        self._holdings.append(holding)

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return self._holdings.__len__()

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    @property
    def holdings(self):
        return self._holdings

    @holdings.setter
    def holdings(self, holdings:list):
        if not isinstance(holdings, list):
            raise TypeError('Expected list')
        self._holdings = holdings

    @property
    def total_cost(self):
        return sum(s.cost for s in self.holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares