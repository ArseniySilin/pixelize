from PIL import Image

filename = 'input.jpg'
pixelSize = 80 
im = Image.open(filename)
pix = im.load()
width = im.size[0]
height = im.size[1]
startX = 0
startY = 0

print('Pixelising...')

while (startX < width and startY < height):
	deltaX = width - startX if startX + pixelSize > width else pixelSize
	deltaY = height - startY if startY + pixelSize > height else pixelSize
	approxListSize = deltaX * deltaY
	allPixelsInQuadrant = []

	for x in range(startX, startX + deltaX):
		for y in range(startY, startY + deltaY):
			allPixelsInQuadrant.append(pix[x, y])

	approxPixels = [sum(x) for x in zip(*allPixelsInQuadrant)]
	approxPixels = [int(x / approxListSize) for x in approxPixels]

	for x in range(startX, startX + deltaX):
		for y in range(startY, startY + deltaY):
			pix[x, y] = tuple(approxPixels)

	startX += pixelSize

	if startX >= width:
		startY = startY + pixelSize
		startX = 0

im.save('output.jpg')

print('Done. Output saved.')
