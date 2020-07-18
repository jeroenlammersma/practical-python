# fileparse.py
#
# Exercise 3.3

from csv import reader

def parse_csv(filename:str, select:list = None,
                types:list = None, has_headers:bool = True,
                delimiter:str = ',', silence_errors:bool = False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = reader(f, delimiter = delimiter)

        if select and not has_headers:
            raise RuntimeError('select argument requires column headers')

        # read the file headers
        if has_headers:
            headers = next(rows)

            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                indices = [ headers.index(colname) for colname in select ]
                headers = select
            else:
                indices = []

        records = []
        for rowno, row in enumerate(rows, start=1):
            if not row: # Skip rows with no data
                continue
            
            # Filter the row if specific columns were selected
            if has_headers and indices:
                row = [ row[index] for index in indices ]

            #convert to type if specific types were provided
            if types:
                try:
                    row = [ func(val) for func, val in zip(types, row) ]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {rowno}: Couldn\'t convert {row}')
                        print(f'Row {rowno}: Reason {e}')
                    continue

            # Make a dictionary or a tuple    
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = row
            records.append(record)
            
        return records

def parse_csv_alt(filename:str, select:list = None, types:list = None):
    '''
    Alternative for parsing a CSV file into a list of records using list
    comprehension
    '''
    with open(filename) as f:
        rows = reader(f)
        
        # read the file headers
        headers = next(rows)

        if not select:
            select = headers
            indices = [ i for i in range(len(headers)) ]
        else:
            indices = [ headers.index(colname) for colname in select ]
        
        if not types:
            types = [ str for i in range(len(headers)) ]

        records = [ {
                        colname: func(row[index])
                        for colname, index, func
                        in zip(select, indices, types)
                        if row[index]
                    } for row in rows ]

    return records