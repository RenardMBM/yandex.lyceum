import pytest
from yandex_testing_lesson import reverse


def test_empty_string():
    assert reverse('') == ''


def test_one_symbol():
    assert reverse('a') == 'a'


def test_palindrome():
    assert reverse('foxof') == 'foxof'


def test_regular_string():
    assert reverse('drofxO') == 'Oxford'


def test_wrong_type_int():
    with pytest.raises(TypeError):
        reverse(42)


def test_wrong_type_list():
    with pytest.raises(TypeError):
        reverse(['d', 'r', 'o', 'f', 'x', 'O'])
