from PIL import Image
import colorsys

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

# colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        h = float(r/255)
        s = float(g/255)
        v = float(b/255)
# do some math on h, s, v

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

# convert back to [0, 255]

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)


#print (r, g, b)

        pixels[i, j] = (r, g, b)

img.show()