import main_functions
import pytest


def test_convert_list_of_lists_to_list_of_dict():
    assert (main_functions.convert_list_of_lists_to_list_of_dict_with_zip([[1, 2, 3], [4, 5, 6]])
            == [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}])
    assert (main_functions.convert_list_of_lists_to_list_of_dict([[1, 2, 3], [4, 5, 6]])
            == [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}])



