# pcost.py
#
# Exercise 1.27

from .report import read_portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    return round(portfolio.total_cost, 2)

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} portfolio')
    print('Total costs:', portfolio_cost(args[1]))

if __name__ == '__main__':
    import sys
    main(sys.argv)
