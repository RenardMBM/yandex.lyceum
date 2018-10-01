def reverse():
    file = open('input.dat', 'rb').read().split()
    newFile = open('output.dat', 'wb')
    a = [i for _ in file for i in _][::-1]
    newFile.write(bytes(a))
    newFile.close()


reverse()
