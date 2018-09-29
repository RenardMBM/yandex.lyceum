def checkTrio(parole: str):
    for indexOfLetter in range(1, len(parole) - 1):
        eng = "qwertyuiop[] asdfghjkl;' zxcvbnm,./"
        rus = 'йцукенгшщзхъ фывапролджэ ячсмитьбю'
        digits = '1234567890-='
        preferLetter = parole[indexOfLetter - 1]
        letter = parole[indexOfLetter]
        nextLetter = parole[indexOfLetter + 1]
        indexOfLetter = 0
        indexOfNextLetter = 0
        indexOfPreferLetter = 0
        if preferLetter.isdigit() and letter.isdigit() and nextLetter.isdigit():
            indexOfPreferLetter = digits.find(preferLetter)
            indexOfLetter = digits.find(letter)
            indexOfNextLetter = digits.find(nextLetter)

        elif not preferLetter.isalpha() or not nextLetter.isalpha() or not letter.isalpha():
            continue

        if 'ё' == preferLetter:
            indexOfPreferLetter = 23
            indexOfLetter += 1 if indexOfLetter < 23 else 0
            indexOfNextLetter += 1 if indexOfNextLetter < 23 else 0

        if 'ё' == nextLetter:
            indexOfNextLetter = 23
            indexOfLetter += 1 if indexOfLetter < 23 else 0
            indexOfPreferLetter += 1 if indexOfNextLetter < 23 else 0

        if 'ё' == letter:
            indexOfLetter = 23
            indexOfPreferLetter += 1 if indexOfPreferLetter < 23 else 0
            indexOfNextLetter += 1 if indexOfNextLetter < 23 else 0

        indexOfLetter += eng.find(letter) if letter in eng else rus.find(letter)
        indexOfPreferLetter += eng.find(preferLetter) if preferLetter in eng else \
            rus.find(preferLetter)
        indexOfNextLetter += eng.find(nextLetter) if nextLetter in eng else rus.find(nextLetter)
        indexes = [indexOfNextLetter, indexOfLetter, indexOfPreferLetter]

        if indexes[0] - 1 == indexes[1] == indexes[2] + 1:
            return False

    return True


def check_password(password):
    exceptions = []
    if len(password) > 8:
        exceptions.append('LengthError')

    isUpper, isLower, isDigit = False, False, False

    for letter in password:
        if letter.isdigit():
            isDigit = True

        elif letter.isupper():
            isUpper = True

        elif letter.islower():
            isLower = True

    if not isDigit:
        exceptions.append('DigitError')

    if not isUpper or not isLower:
        exceptions.append('LetterError')

    if not checkTrio(password.lower()):
        exceptions.append('SequenceError')

    return exceptions


exceptions = {}  # NameOfError : number
try:
    assert not check_password(input())
    print('ok')
    for exception in exceptions.keys():
        print(exception, exceptions[exception], sep=' = ')

except AssertionError:
    print('error')
