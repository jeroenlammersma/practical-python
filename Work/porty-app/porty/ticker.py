# ticker.py

from .follow import follow
from .tableformat import create_formatter
from .report import read_portfolio
import csv
import sys

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)

def filter_symbols(rows, names):
    return (row for row in rows if row['name'] in names)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfolio, logfile, fmt):
    portfolio = read_portfolio(portfolio)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    formatter = create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )

def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: %s portfolio logfile format' % args[0])
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    main(sys.argv)