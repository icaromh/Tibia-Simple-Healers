from PIL import Image


class getPixelsInImage():

    def __init__(self, image):
        self.image = image

    def getPixelsHealth(self):
        im = Image.open(self.image)
        red = 0

        for pixel in im.getdata():
            if pixel == (219, 79, 79):
                red += 1
        
        if red > 0:
            return red
        else:
            return 0
        
    def getPixelsMana(self):
        im = Image.open(self.image)
        blue = 0

        for pixel in im.getdata():
            if pixel == (83, 80, 218):
                blue += 1
        
        if blue > 0:
            return blue
        else:
            return 0

       