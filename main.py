from PIL import Image

# Отваряме снимката
img = Image.open('image.png')
pixels = img.load()
# Взимаме размерите на изображението
width, height = img.size

scale, offset = 35, 0
filterGrid = [[1,1,1,1,1],
             [1,2,2,2,1],
             [1,2,3,2,1],
             [1,2,2,2,1],
             [1,1,1,1,1]]
# Създаваме копие за да не променяме оригиналните стойности
filteredImg = img.copy()
filteredPixels = filteredImg.load()

for x in range(width):
    for y in range(height):
        new_pixel = [0, 0, 0]
        for rgb in range(0,3):
            pixel_sum = 0
            for i in range(0,5):
                for j in range(0,5):
                    xi, yj = x+i, y+j
                    # if-а проверява дали координатите на пикселите са в допустимите стойности
                    # вадим от всичко -2 за да нагодим стойности от филтъра на пикселите
                    if 0 <= xi-2 < width and 0 <= yj-2 < height:
                        pixel_sum += pixels[xi-2 , yj-2][rgb] * filterGrid[i][j]
            new_pixel[rgb] = max(0, min(255, int(pixel_sum / scale + offset)))
        filteredPixels[x, y] = tuple(new_pixel)



filteredImg.save('GaussianBlur.png')