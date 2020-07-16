# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                holding = {
                    'name'  : record['name'],
                    'shares': int(record['shares']),
                    'price' : float(record['price'])
                }
                portfolio.append(holding)
            except ValueError:
                print(f'Row {rowno}: Can\'t parse {row}')
    
    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

def make_report(portfolio, prices):
    report = []

    for s in portfolio:
        report.append(
            (
                s['name'],
                s['shares'],
                s['price'],
                prices.get(s['name']) - s['price']
            )
        )

    return report
    
def print_report():
    portfolio = read_portfolio('Data\portfoliodate.csv')
    prices    = read_prices('Data\prices.csv')

    report = make_report(portfolio, prices)
    
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

print_report()

portfolio = read_portfolio('Data\portfoliodate.csv')
prices    = read_prices('Data\prices.csv')

