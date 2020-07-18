# pcost.py
#
# Exercise 1.27

import csv, sys
from report import read_portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    return round(sum([s['shares'] * s['price'] for s in portfolio]), 2)

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data\portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total costs:', cost)
