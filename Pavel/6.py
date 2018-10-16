from yandex_testing_lesson import strip_punctuation_ru


def test():
    tests = {'ФапвлплвФФ,...аап, апав?!! Вввв': 'ФапвлплвФФ аап апав Вввв', '': ''}
    for test in tests.keys():
        if strip_punctuation_ru(test) != tests[test]:
            return 'NO'
    return 'YES'


print(test())
