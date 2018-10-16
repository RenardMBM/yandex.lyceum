from yandex_testing_lesson import is_palindrome


print('YES' if [True, True, True, False, False, True, True, False, False, False] == [
    is_palindrome(string)
    for string in['', 'a', 'aa', 'aab', 'abcd', 'abba', 'a c b b c a', 'тррря', 'утка', 'кот']
] else 'NO')
