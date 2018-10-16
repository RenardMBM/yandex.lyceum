from json import load

with open('scoring.json') as file:
    tests = load(file)['scoring']
    costOfTests = dict()

    for test in tests:
        costOfTests[','.join([str(n) for n in test['required_tests']])] = int(test['points'])
    answers = [key for groupOfKeys in costOfTests.keys()
               for key in groupOfKeys.split(',')
               if input() == 'ok']

    total = 0

    for groupOfTests in costOfTests.keys():
        result = True

        for testName in groupOfTests.split(','):

            if testName in answers:
                continue

            else:
                result = False
                break

        if result:
            total += costOfTests[groupOfTests]

    print(total)
