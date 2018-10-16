from yandex_testing_lesson import is_under_queen_attack
import pytest


def test_regular_value():
    assert is_under_queen_attack('a7', 'b6')

    assert not is_under_queen_attack('h7', 'a2')

    assert is_under_queen_attack('g8', 'g8')

    assert is_under_queen_attack('a1', 'h8')


def test_upper_letter():
    with pytest.raises(ValueError):
        is_under_queen_attack('A1', 'A8')


def test_wrong_position():
    with pytest.raises(ValueError):
        is_under_queen_attack('a9', 'h1')


def test_wrong_queen_position():
    with pytest.raises(ValueError):
        is_under_queen_attack('a3', 'a0')


def test_position_of_number():
    with pytest.raises(ValueError):
        is_under_queen_attack('11', 'a1')


def test_queen_position_of_number():
    with pytest.raises(ValueError):
        is_under_queen_attack('a2', '74')


def test_wrong_format_of_position():
    with pytest.raises(ValueError):
        is_under_queen_attack('1a', 'g5')


def test_wrong_format_of_queen_position():
    with pytest.raises(ValueError):
        is_under_queen_attack('d7', '6d')


def test_wrong_position_int():
    with pytest.raises(TypeError):
        is_under_queen_attack(0, 'a6')


def test_wrong_queen_position_int():
    with pytest.raises(TypeError):
        is_under_queen_attack('d4', 100)


def test_wrong_position_list():
    with pytest.raises(TypeError):
        is_under_queen_attack(['a', '5'], 'e7')


def test_wrong_queen_position_list():
    with pytest.raises(TypeError):
        is_under_queen_attack('g8', ['e', '4'])


def test_wrong_length():
    with pytest.raises(ValueError):
        is_under_queen_attack('f8a4', 'b4')
