from PIL import Image
from settings import ROW, COLUMN

imageOfCell = Image.open('closed_cell.png')
cellX, cellY = imageOfCell.size
cellRGB = imageOfCell.load()
cellX, cellY = cellX - 1, cellY - 1
# print(cellX, cellY)

imageOfMap = Image.new('RGB', (cellX * COLUMN, cellY * ROW), (0, 0, 0))
mapX, mapY = imageOfMap.size
mapRGB = imageOfMap.load()

for x in range(mapX):

    for y in range(mapY):
        x1 = x % cellX if x > cellX else x
        y1 = y % cellY if y > cellY else y

        mapRGB[x, y] = cellRGB[x1, y1]

imageOfMap.save('map.png')
