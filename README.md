# MerbuzPixel

**MerbuzPixel** is an improved version of the **neopixel** library, which is available in MicroPython by default. A 16x16 matrix was tested on a **Wemos Mini d1 r1** microcontroller.

## How it use?

Just **download the library file** and import it into your board!

## Code

Example of using the library

```python
import merbuzpixel
from machine import Pin

p = Pin(4, Pin.OUT)

merbuz = MerbuzPixel(p, 256) # Create class. first - pin of matrix, second - count of leds
merbuz.setBrightness(10) # Set brightness 0-255

merbuz.setPixel(i, (255, 255, 255)) # Set pixel, first - index, second - tuple of RGB

merbuz.clearMatrix() # Just clear matrix. All

merbuz.fillPixels(6, 70, (255, 255, 255)) # Fill by index led. First - index of first led, second - index of second led, third - tuple of RGB

merbuz.fillBackground((255, 255, 255)) # Fill all matrix

merbuz.clearPixel(0) # Pixel index to clear
```





