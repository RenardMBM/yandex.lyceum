with open('input.bmp', 'rb') as bmpFile:
    first = bmpFile.read(54)
    end = bmpFile.read()

with open('res.bmp', 'wb') as newFile:
    newFile.write(first + bytes([255 - int(chr(_)) for _ in end]))