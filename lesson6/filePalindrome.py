def palindrome():
    text = open('input.dat', 'rb').read().split()
    a = [i for _ in text for i in _]
    return a[:len(a) // 2] == a[-1 * (len(a) // 2):][::-1] if len(a) > 1 else True
