import mip # Import mip for install neopixel

mip.install('neopixel')

import neopixel 

class MerbuzPixel:
    def __init__(self, pin, leds):
        self.pin = pin # pin for the connect led
        self.leds = leds # count of leds
        self.brightness = 1 # default brightness
        
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
        # Send text 
        for i in range(self.leds):
            self.np[i] = (0,0,0)
        self.np.write()
    
    def clearPixel(self, index):
        if index > self.leds:
            raise Exception('Index must be more or less than count of leds')
        self.np[index] = (0,0,0)
        self.np.write()
