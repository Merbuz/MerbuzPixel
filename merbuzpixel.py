import mip # Import mip for install neopixel

mip.install('neopixel')

import neopixel
import micropython
from io import open
from machine import Pin

class MerbuzPixel:
    # Default colors

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 128, 0)
    YELLOW = (255, 255, 0)
    LIGHTBLUE = (0, 255, 255)
    WHITE = (255, 255, 255)
    VIOLET = (127, 0, 255)
    PURPLE = (255, 0, 255)
    PINK = (255, 0, 127)
    
    def __init__(self, pin, width, height):
        self.pin = Pin(pin, Pin.OUT) # pin for the connect led
        self.width = width # width of matrix
        self.height = height # height of matrix

        self.brightness = 1.0 # default brightness
        self.leds = self.width * self.height 
        self.np = neopixel.NeoPixel(self.pin, self.leds, 3)

    def setBrightness(self, brightness):
        # Brightness range is 0-255

        if brightness < 0 or brightness > 255:
            raise Exception('Brightness must be in range 0-255')

        self.brightness = brightness/255
        
    def setPixel(self, index, rgb):
        # Set color of pixel

        for value in rgb:
            if value > 255 or value < 0:
                raise Exception('Red, green and blue must be more than 0 and less than 255')
        
        self.np[index] = (int(rgb[0] * self.brightness), int(rgb[1] * self.brightness), int(rgb[2] * self.brightness))
        self.np.write()
    
    def fillPixels(self, firstIndex, secondIndex, rgb):
        # Fill some range of selected color

        for i in range(firstIndex, secondIndex):
            self.np[i] = (int(rgb[0] * self.brightness), int(rgb[1] * self.brightness), int(rgb[2] * self.brightness))
        self.np.write()
    
    def fillBackground(self, rgb):
        # Fill all matrix of selected color

        for i in range(self.leds):
            self.np[i] = (int(rgb[0] * self.brightness), int(rgb[1] * self.brightness), int(rgb[2] * self.brightness))
        self.np.write()
    
    def clearMatrix(self):
        # Clear all matrix

        for i in range(self.leds):
            self.np[i] = (0,0,0)
        self.np.write()
    
    def clearPixel(self, index):
        # Clear current pixel

        if index > self.leds:
            raise Exception('Index more than count of leds')
        self.np[index] = (0,0,0)
        self.np.write()
    
    def drawImage(self, file_name):
        # This method use file with .merbuzpixel extension where is the picture encoded
        # Draw image method
        
        with open(file_name, 'r') as file:
            try:
                file_lines = file.readlines()
                for lines in file_lines:
                    lines = lines.replace('(','').split(')')
                    for line in lines:
                        R, G, B, index = int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2]), int(line.split(',')[3])
                        self.np[index] = (int(R * self.brightness), int(G * self.brightness), int(B * self.brightness))
                        
            except:
                self.np.write()
