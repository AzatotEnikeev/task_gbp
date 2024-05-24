import main_functions as main
import pytest


test_value = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]


def test_calc_count_in_list_of_sets():
    assert (main.calc_count_in_list_of_sets(test_value) == 14)


def test_calc_sum_in_list_of_sets():
    assert (main.calc_sum_in_list_of_sets(test_value) == 264)


def test_calc_average_in_list_of_sets():
    assert (main.calc_average_in_list_of_sets(test_value) == 18.857142857142858)


def test_convert_list_of_sets_to_tuple():
    assert (main.convert_list_of_sets_to_tuple(test_value) == (11, 3, 5, 32, 17, 2, 87, 4, 44, 7, 8, 9, 11, 24))