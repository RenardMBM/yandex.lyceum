def is_prime(n):
    if type(n) != int:
        # check type
        raise TypeError()
    elif n <= 1:
        # check
        raise ValueError()

    # error was here: range(2, k) doesn't include k
    # hence, for example, for 9 only divisor 2 will be checked
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True

print(is_prime(9s))