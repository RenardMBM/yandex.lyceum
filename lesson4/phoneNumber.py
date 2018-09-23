def checkPhoneNumber(phone_number):
    phoneNumber = ''.join(phone_number.split())
    if phoneNumber[0] == '8':
        phoneNumber = phoneNumber[1:]

    elif phoneNumber[0] == '+' and phoneNumber[1] == '7':
        phoneNumber = phoneNumber[2:]

    else:
        return 'error'

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
                return 'error'

        return '+7' + ''.join(correctPhoneNumber) \
            if not isLastMinus and len(correctPhoneNumber) == 10 else 'error'

    else:
        return 'error'


print(checkPhoneNumber(input()))
