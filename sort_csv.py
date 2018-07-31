#!/usr/bin/env python3

import argparse
import csv
from typing import List


def get_row_list_from_csv_file(filename: str) -> List[str]:
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        return next(reader)


def sort_row_list(row_list: List[str], reverse: bool = True) -> List[str]:
    return sorted(row_list, reverse=reverse)


def convert_list_to_row_str(row_list: List[str]) -> str:
    return ','.join(row_list)


def write_row_str_to_file(row_str: str, filename: str) -> None:
    with open(filename, 'w') as f:
        f.write(f'{row_str}\n')


def sort_csv_file(infile: str, outfile: str) -> None:
    row_list = get_row_list_from_csv_file(filename=infile)
    row_list = sort_row_list(row_list=row_list)
    row_str = convert_list_to_row_str(row_list=row_list)
    write_row_str_to_file(row_str=row_str, filename=outfile)


def main() -> None:
    parser = argparse.ArgumentParser(description='Cambia Takehome Interview: CSV Sort')
    parser.add_argument('-in', '--infile',
                        metavar='IN_FILE',
                        required=False,
                        default=None,
                        help='The filename of the input csv')
    parser.add_argument('-out', '--outfile',
                        metavar='OUT_FILE',
                        required=False,
                        default=None,
                        help='The filename of the output csv')
    cli_args = parser.parse_args()

    infile = cli_args.infile if cli_args.infile else input('Enter an input filename: ')
    outfile = cli_args.outfile if cli_args.outfile else input('Enter an output filename: ')

    sort_csv_file(infile=infile, outfile=outfile)


if __name__ == '__main__':
    main()
