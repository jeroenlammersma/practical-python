import csv
import datetime
from pprint import pprint

def read_vehicles(filename):
    vehicles = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f, delimiter=';')
        headers = next(rows)
        # select = ['KENTEKEN', 'MERK', 'HANDELSBENAMING']
        types = [int, str, int, str, str, str, str, str, str, float, str, int, str, float, int]
        # types = [str, str, str]
        indices = [ headers.index(colname) for colname in headers ]
        print(indices)

        try:
            vehicles = [ { colname: func(row[index]) for colname, index, func, val in zip(headers, indices, types, row) if val } for row in rows ]
        except ValueError:
            print('Can\'t parse')
        return vehicles

vehicles = read_vehicles('Self\DWH_VOERTUIG.csv')
pprint(vehicles)