class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def checkTrio(parole: str):
    for indexOfLetter in range(1, len(parole) - 1):
        eng = 'qwertyuiopasdfghjklzxcvbnm------'
        rus = 'йцукенгшщзхъфывапролджэячсмитьбю'
        preferLetter = parole[indexOfLetter - 1]
        letter = parole[indexOfLetter]
        nextLetter = parole[indexOfLetter + 1]
        indexOfLetter = 0
        indexOfNextLetter = 0
        indexOfPreferLetter = 0

        if preferLetter.isdigit() or nextLetter.isdigit() or letter.isdigit():
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
        indexOfPreferLetter += eng.find(preferLetter) if preferLetter in eng else\
            rus.find(preferLetter)
        indexOfNextLetter += eng.find(nextLetter) if nextLetter in eng else rus.find(nextLetter)
        indexes = sorted([indexOfNextLetter, indexOfLetter, indexOfPreferLetter])

        if indexes[0] + 1 == indexes[1] == indexes[2] - 1:
            return False

    return True


def check_password(password):
    if len(password) >= 8:
        isUpper, isLower, isDigit = False, False, False

        for letter in password:
            if letter.isdigit():
                isDigit = True

            elif letter.isupper():
                isUpper = True

            elif letter.islower():
                isLower = True

        if not isDigit:
            raise DigitError

        elif not isUpper or not isLower:
            raise LetterError

        elif not checkTrio(password.lower()):
            raise SequenceError

        else:
            print('ok')

    else:
        raise LengthError


try:
    check_password(input())
except LetterError or LengthError or SequenceError or DigitError:
    print('error')
