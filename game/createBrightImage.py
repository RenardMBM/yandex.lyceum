from PIL import Image

sourceName = input()
source = Image.open(sourceName)
sourceX, sourceY = source.size
sourceRGB = source.load()

res = Image.new('RGB', (sourceX, sourceY), (0, 0, 0))
resRGB = res.load()

for x in range(sourceX):

    for y in range(sourceY):
        rgb = sourceRGB[x, y]
        resRGB[x, y] = (rgb[0] + 30, rgb[1] + 30, rgb[2] + 30)

res.save('images/bright_' + sourceName.split('/')[-1])
