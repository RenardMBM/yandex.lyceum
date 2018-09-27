class UncorrectedPhoneNumber(Exception):
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

    def checkPhoneNumber(phone_number):
        phoneNumber = ''.join(phone_number.split())
        if phoneNumber[0] == '8':
            phoneNumber = phoneNumber[1:]

        elif phoneNumber[0] == '+' and phoneNumber[1] == '7':
            phoneNumber = phoneNumber[2:]

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
                    raise NonExistentOperator

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

    except NonExistentOperator:
        print('не определяется оператор сотовой связи')


main()
