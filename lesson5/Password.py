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
        indexOfPreferLetter += eng.find(preferLetter) if preferLetter in eng else\
            rus.find(preferLetter)
        indexOfNextLetter += eng.find(nextLetter) if nextLetter in eng else rus.find(nextLetter)
        indexes = sorted([indexOfNextLetter, indexOfLetter, indexOfPreferLetter])

        if indexes[0] + 1 == indexes[1] == indexes[2] - 1:
            return False

    return True


def checkWord(parole: str):
    words = open("top-9999-words.txt").read().split()
    for word in words:
        if word in parole:
            return True
    else:
        return False


def check_password(password):
    errors = []
    if len(password) > 8:
        errors.append('LengthError')
    isUpper, isLower, isDigit = False, False, False

    for letter in password:
        if letter.isdigit():
            isDigit = True

        elif letter.isupper():
            isUpper = True

        elif letter.islower():
            isLower = True

    if not isDigit:
        errors.append('DigitError')

    if not isUpper or not isLower:
        errors.append('LetterError')

    if not checkTrio(password.lower()):
        errors.append('SequenceError')

    if not checkWord(password.lower()):
        errors.append('WordError')

    return errors


exceptions = {'LengthError': 0,
              'DigitError': 0,
              'LetterError': 0,
              'SequenceError': 0,
              'WordError': 0}  # NameOfError : number
# while True:
passwords = open('top 10000 passwd.txt').read().split()

for text in passwords:
    try:
        global errors
        # text = input()
        if text == 'Ctrl+Break':
            raise KeyboardInterrupt

        errors = check_password(text)
        assert not errors

    except AssertionError:
        for error in errors:
            exceptions[error] += 1

    except KeyboardInterrupt:
        print('Bye-Bye')

        for exception in exceptions.keys():
            print(exception, exceptions[exception], sep=' = ')

for exception in exceptions.keys():
    print(exception, exceptions[exception], sep=' = ')
