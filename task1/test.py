import csv
import main

def test_get_unique_records():
    dict_unique_records = main.get_unique_records("test.txt")
    assert (len(dict_unique_records) == 4)

def test_get_duplicate_records():
    dict_unique_records = main.get_duplicate_records("test.txt")
    assert (len(dict_unique_records) == 4)

