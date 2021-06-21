from PIL import Image

def negative(img:Image)->Image:
    neg = Image.new(img.mode, img.size, "red")

    w, h = img.size
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i, j)) 
            neg.putpixel((i, j), (255-r, 255-g, 255-b))
    return neg

img = Image.open("images/bnha.jpg")
negative(img).show()