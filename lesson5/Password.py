def main():
    def checkTrio(parole: str):
        for indexOfLetter in range(1, len(parole) - 1):
            eng = 'qwertyuiopasdfghjklzxcvbnm------'
            rus = 'йцукенгшщзхъфывапролджэячсмитьбю'
            preferLetter = parole[indexOfLetter - 1]
            nextLetter = parole[indexOfLetter + 1]
            indexOfNextLetter = 0
            indexOfPreferLetter = 0

            if preferLetter.isdigit() or nextLetter.isdigit() or parole[indexOfLetter].isdigit():
                continue

            if 'ё' == preferLetter:
                indexOfPreferLetter = 23
                indexOfLetter += 1 if indexOfLetter < 23 else 0
                indexOfNextLetter += 1 if indexOfNextLetter < 23 else 0

            if 'ё' == nextLetter:
                indexOfNextLetter = 23
                indexOfLetter += 1 if indexOfLetter < 23 else 0
                indexOfPreferLetter += 1 if indexOfNextLetter < 23 else 0

            if 'ё' == parole[indexOfLetter]:
                indexOfLetter = 23
                indexOfPreferLetter += 1 if indexOfPreferLetter < 23 else 0
                indexOfNextLetter += 1 if indexOfNextLetter < 23 else 0

            indexOfPreferLetter += eng.find(preferLetter) if preferLetter in eng else \
                rus.find(preferLetter) if preferLetter in rus else 0
            indexOfNextLetter += eng.find(nextLetter) if nextLetter in eng else \
                rus.find(nextLetter) if nextLetter in rus else 0
            indexes = sorted([indexOfNextLetter, indexOfLetter, indexOfPreferLetter])

            if indexes[0] + 1 == indexes[1] == indexes[2] - 1:
                return False

        return True

    def checkPassword(password):
        if len(password) >= 8:
            isUpper, isLower, isDigit = False, False, False

            for letter in password:
                if letter.isdigit():
                    isDigit = True

                elif letter.isupper():
                    isUpper = True

                elif letter.islower():
                    isLower = True

            return 'ok' if (isDigit and
                            isUpper and
                            isLower and
                            checkTrio(password.lower())) else 'error'

        else:
            return 'error'

    print(checkPassword(input()))


main()
