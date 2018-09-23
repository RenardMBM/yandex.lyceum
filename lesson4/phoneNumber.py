def checkPhoneNumber(phone_number):
    phoneNumber = ''.join(phone_number.split())
    if phoneNumber[0] == '8':
        phoneNumber = phoneNumber[1:]
    elif phoneNumber[0] == '+' and phoneNumber[1] == '7':
        phoneNumber = phoneNumber[2:]
    else:
        return 'error'

    if phoneNumber.count('(') == phoneNumber.count(')'):
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

        return '+7' + ''.join(correctPhoneNumber)
    else:
        return 'error'


print(checkPhoneNumber(input()))
