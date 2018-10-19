from yandex_testing_lesson import Rectangle
import random
import pytest


def test_regular_value():
    instance = Rectangle(2, 4)

    assert instance.get_area() == 8
    assert instance.get_perimeter() == 12


def test_zero():
    instance = Rectangle(0, 1)

    assert not instance.get_area()
    assert instance.get_perimeter() == 2


def test_type_float():
    instance = Rectangle(0.1, 0.9)

    assert instance.get_area() == 0.09000000000000001
    assert instance.get_perimeter() == 2


def test_wrong_type_str():
    with pytest.raises(TypeError):
        Rectangle('0', '7')


def test_negative_number():
    with pytest.raises(ValueError):
        Rectangle(-1, 0)


def test_fractional_negative_number():
    with pytest.raises(ValueError):
        Rectangle(-0.00000000000001, 0.000001)
