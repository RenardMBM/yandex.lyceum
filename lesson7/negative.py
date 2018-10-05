with open('input.bmp', 'rb') as bmpFile:
    with open('res.bmp', 'wb') as newFile:
        newFile.write(bmpFile.read(54))
        newFile.write(list(255 - int(chr(_)) for _ in bmpFile.read()))
