# fileparse.py

import logging
from csv import reader

log = logging.getLogger(__name__)

def parse_csv(lines, select:list = None,
                types:list = None, has_headers:bool = True,
                delimiter:str = ',', silence_errors:bool = False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    rows = reader(lines, delimiter = delimiter)

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
                    log.warning(f'Row {rowno}: Couldn\'t convert {row}')
                    log.debug(f'Row {rowno}: Reason {e}')
                continue

        # Make a dictionary or a tuple    
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = row
        records.append(record)
        
    return records