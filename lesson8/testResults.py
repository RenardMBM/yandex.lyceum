from json import load

with open('scoring.json') as file:
    tests = load(file)['scoring']

    costOfTests = dict()

    for test in tests:
        print(test)
        for testNumber in test['required_tests']:
            costOfTests[str(testNumber)] = test['points']

    total = 0

    for k in [key for key in costOfTests.keys()]:
        total += costOfTests[k] if input() == 'ok' else 0

    print(costOfTests)
    print(total)
