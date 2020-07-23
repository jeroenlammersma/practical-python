# report.py

from . import stock
from . import tableformat
from .fileparse import parse_csv
from .portfolio import Portfolio

def read_portfolio(filename:str, **opts:dict):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)

def read_prices(filename:str, **opts):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False, **opts))

def make_report(portfolio:list, prices:dict):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = [ (s.name, s.shares, s.price, prices.get(s.name) - s.price) for s in portfolio ]
    return report
    
def print_report(reportdata:list, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfoliofile:str, pricefile:str, fmt:str='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''

    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices    = read_prices(pricefile)

    # Create the report data
    report    = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) == 3:
        portfolio_report(args[1], args[2])
    elif len(args) == 4:
        portfolio_report(args[1], args[2], args[3])
    else:
        raise SystemExit(f'Usage: {args[0]} portfolio pricefile format')
    
if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename = 'app.log',
        filemode = 'w',
        level = logging.DEBUG
    )
    
    import sys
    main(sys.argv)
