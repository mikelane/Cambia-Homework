import os
import pytest

import sort_csv


def test_get_row_list_from_csv_file():
    assert sort_csv._get_row_list_from_csv_file(filename='tests/test_csv_1.csv') == ['Copenhagen', 'Stockholm', 'Oslo']
    with pytest.raises(FileNotFoundError):
        sort_csv._get_row_list_from_csv_file(filename='not_there.csv')
    assert sort_csv._get_row_list_from_csv_file(filename='tests/test_csv_2.csv') == ['2', '3', '1']


def test_sort_row_list():
    assert sort_csv._sort_row_list(row_list=['Copenhagen', 'Stockholm', 'Oslo']) == ['Stockholm', 'Oslo', 'Copenhagen']
    assert sort_csv._sort_row_list(row_list=[]) == []
    assert sort_csv._sort_row_list(row_list=['']) == ['']
    assert sort_csv._sort_row_list(row_list=['a', '1', 'b', '2']) == ['b', 'a', '2', '1']


def test_convert_list_to_row_str():
    assert sort_csv._convert_list_to_row_str(
        row_list=['Stockholm', 'Oslo', 'Copenhagen']) == 'Stockholm,Oslo,Copenhagen'
    assert sort_csv._convert_list_to_row_str(row_list=['1234,', ',,,', 'asdf']) == '1234,,,,,,asdf'


def test_write_row_str_to_file():
    sort_csv._write_row_str_to_file(row_str='Stockholm,Oslo,Copenhagen', filename='tests/test_output_1.csv')
    with open(file='tests/test_output_1.csv', mode='r') as f:
        assert f.read() == 'Stockholm,Oslo,Copenhagen\n'
    os.remove('tests/test_output_1.csv')


def test_sort_csv_file():
    sort_csv.sort_csv_file(infile='csv_files/test1.csv', outfile='csv_files/test_out1.csv')
    with open(file='csv_files/test_out1.csv', mode='r') as f:
        assert f.read().strip() == 'Stockholm,Oslo,Copenhagen'
    os.remove('csv_files/test_out1.csv')
