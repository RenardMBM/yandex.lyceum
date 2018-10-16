from yandex_testing_lesson import is_prime


print('YES' if [True, True, True, False, False] == [
    is_prime(number) for number in [991, 907, 2, 272, 1833]
] else 'NO')
