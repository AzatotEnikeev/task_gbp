import main
import pytest

dict_words = main.create_dict_from_file("test.txt")


def test_task5_find_combine_second_word():
    assert(main.find_combine_second_word('ласты', dict_words) == ['ластык', 'ластыковка'])
    assert (main.find_combine_second_word('кабала', dict_words) == ['кабаласты', 'кабаласт'])
    assert (main.find_combine_second_word('стыковка', dict_words) == ['стыковкабала', 'стыковкарась'])


