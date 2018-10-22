from PIL import Image


class getPixelsInImage():

    def __init__(self, image):
        self.image = image

    def getPixelsHealth(self):
        im = Image.open(self.image)
        red = 0

        for pixel in im.getdata():
            if pixel == (241, 97, 97):
                red += 1
        
        if red > 0:
            return red
        else:
            return 0
        
    def getPixelsMana(self):
        im = Image.open(self.image)
        blue = 0

        for pixel in im.getdata():
            if pixel == (82, 79, 211):
                blue += 1
        
        if blue > 0:
            return blue
        else:
            return 0

       