#!/usr/bin/env python3

import argparse
import csv
import log
from typing import List

logger = log.get_logger(__name__)


def _get_row_list_from_csv_file(filename: str) -> List[str]:
    logger.debug(f'Looking for csv file {filename}')
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        logger.debug(f'Found {filename}, returning first row.')
        return next(reader)


def _sort_row_list(row_list: List[str], reverse: bool = True) -> List[str]:
    logger.debug('Sorting the row list.')
    return sorted(row_list, reverse=reverse)


def _convert_list_to_row_str(row_list: List[str]) -> str:
    logger.debug('Converting row list to a string')
    return ','.join(row_list)


def _write_row_str_to_file(row_str: str, filename: str) -> None:
    logger.debug(f'Writing to output file {filename}')
    with open(filename, 'w') as f:
        f.write(f'{row_str}\n')


def sort_csv_file(infile: str, outfile: str) -> None:
    try:
        _write_row_str_to_file(
            row_str=_convert_list_to_row_str(
                row_list=_sort_row_list(
                    row_list=_get_row_list_from_csv_file(filename=infile))),
            filename=outfile)
    except FileNotFoundError as e:
        logger.error(f'ERROR: {e}')


def _get_cli_args() -> argparse.Namespace:
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
    return parser.parse_args()


def main() -> None:
    cli_args = _get_cli_args()
    logger.debug(f'Got CLI arguments: {cli_args}')

    infile = cli_args.infile if cli_args.infile else input('Enter an input filename: ')
    outfile = cli_args.outfile if cli_args.outfile else input('Enter an output filename: ')

    logger.debug(f'Running sort_csv_file(infile={infile}, outfile={outfile})')
    sort_csv_file(infile=infile, outfile=outfile)


if __name__ == '__main__':
    main()
