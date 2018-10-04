with open('wares.csv') as file:

    for string in file:
        name, preferCost, newCost = string.split(';')

        if not preferCost.isdigit():
            continue

        if int(preferCost) > int(newCost):
            print(name)
