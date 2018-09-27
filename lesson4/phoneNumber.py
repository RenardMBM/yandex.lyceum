class UncorrectedPhoneNumber(Exception):
    pass


class UncorrectedLength(Exception):
    pass


class NonExistentOperatorCod(Exception):
    pass


class NonExistentCountryCod(Exception):
    pass


def main():
    def checkOperatorCodes(number):
        cod = []
        _ = 0
        while len(cod) < 3:
            symbol = number[_]
            _ += 1
            if symbol.isdigit():
                cod.append(symbol)

        cod = int(''.join(cod))
        return 901 < cod < 907 or 909 < cod < 940 or 959 < cod < 970 or 979 < cod < 990

    def checkCountryCodes(number):
        if number[:2] == '+1' or number[:3] == '+55' or number[:4] == '+359':
            return number

        else:
            return False

    def checkPhoneNumber(phone_number):
        phoneNumber = ''.join(phone_number.split())
        if phoneNumber[0] == '8':
            phoneNumber = phoneNumber[1:]

        elif phoneNumber[0] == '+':
            if phoneNumber[:2] == '+7':
                phoneNumber = phoneNumber[2:]

            else:
                phoneNumber = checkCountryCodes(phoneNumber)

                if not phoneNumber:
                    raise NonExistentCountryCod

                else:
                    return phoneNumber

        else:
            raise UncorrectedPhoneNumber

        openCount, closeCount = phoneNumber.count('('), phoneNumber.count(')')

        if openCount == closeCount and (openCount == 1 or closeCount == 0):
            correctPhoneNumber = []
            isLastMinus = False

            for symbol in phoneNumber:
                if symbol.isdigit():
                    correctPhoneNumber.append(symbol)
                    isLastMinus = False

                elif symbol == '-' and not isLastMinus:
                    isLastMinus = True
                    continue

                elif symbol == '(' or symbol == ')':
                    continue

                else:
                    raise UncorrectedPhoneNumber

            if not isLastMinus:
                if len(correctPhoneNumber) != 10:
                    raise UncorrectedLength

                if not checkOperatorCodes(phoneNumber):
                    raise NonExistentOperatorCod

                return '+7' + ''.join(correctPhoneNumber)
            else:
                raise UncorrectedPhoneNumber
        else:
            raise UncorrectedPhoneNumber

    try:
        print(checkPhoneNumber(input()))
    except UncorrectedPhoneNumber:
        print('неверный формат')

    except UncorrectedLength:
        print('неверное количество цифр')

    except NonExistentOperatorCod:
        print('не определяется оператор сотовой связи')

    except NonExistentCountryCod:
        print('не определяется код страны')


main()
