# report.py
#
# Exercise 2.4

from fileparse import parse_csv

def read_portfolio(filename:str):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])

def read_prices(filename:str):
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))

def make_report(portfolio:list, prices:dict):
    report = [ (s['name'], s['shares'], s['price'], prices.get(s['name']) - s['price']) for s in portfolio ]
    return report
    
def print_report(report:list): 
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def portfolio_report(portfolio_filename: str, prices_filename: str):
    portfolio = read_portfolio(portfolio_filename)
    prices    = read_prices(prices_filename)
    report    = make_report(portfolio, prices)
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} portfolio pricefile')
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
