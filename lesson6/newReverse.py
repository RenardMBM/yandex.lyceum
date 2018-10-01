def reverse():
    file = open('input.dat', 'rb').read()
    newFile = open('output.dat', 'wb')
    print(file)
    # a = []
    # for _ in file:
    #     a.append(_)
    #     print(_)
    a = [_ for _ in file][::-1]
    newFile.write(bytes(a))
    newFile.close()


reverse()
