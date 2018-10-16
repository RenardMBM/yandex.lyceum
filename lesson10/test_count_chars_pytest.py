from yandex_testing_lesson import count_chars
import pytest


def test_wrong_type_int():
    with pytest.raises(TypeError):
        count_chars(413)


def test_wrong_type_list():
    with pytest.raises(TypeError):
        count_chars(['f', 'o', 'x', 'o', 'r', 'c', 'a', 't'])


def test_one_symbol():
    assert count_chars('f') == {'f': 1}


def test_regular_string():
    assert count_chars('foxorcat') == {'f': 1,
                                       'o': 2,
                                       'x': 1,
                                       'r': 1,
                                       'c': 1,
                                       'a': 1,
                                       't': 1} 