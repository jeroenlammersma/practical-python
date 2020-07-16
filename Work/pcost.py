# pcost.py
#
# Exercise 1.27

import csv, sys

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += (nshares * price)
            except ValueError:
                print(f'Row {rowno}: Couldn\'t convert: {row}')
        
        total_cost = round(total_cost, 2)

        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data\portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total costs:', cost)
