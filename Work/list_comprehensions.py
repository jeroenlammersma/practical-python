# list comprehensions exercise

import csv
import datetime as dt
from pprint import pprint

def read_portfolio(filename):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        
        select = [ 'name', 'price', 'shares' ]
        types = [str, float, int]
        indices = [ headers.index(colname) for colname in select ]
        print(indices)
        
        portfolio = [ { name: func(row[index]) for name, index, func in zip(select, indices, types) } for row in rows ]
        
        return portfolio

def read_dowstocks(filename):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)

        types = [str, float, str, str, float, float, float, float, int]
        portfolio = [
                        {
                            colname: dt.datetime.strptime(val, '%d/%m/%Y').date() if colname == 'date'else func(val)
                            for colname, func, val
                            in zip(headers, types, row)
                        }
                        for row in rows
                    ]

        return portfolio

# portfolio = read_portfolio('Data\portfoliodate.csv')
# pprint(portfolio)

portfolio_dow = read_dowstocks('Data\dowstocks.csv')
pprint(portfolio_dow)