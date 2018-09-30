def reverse():
    file = open('input.dat', 'rb').read()
    newFile = open('output.dat', 'wb')
    print(file[::-1], file=newFile)

    newFile.close()
