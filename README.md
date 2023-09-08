# MerbuzPixel

**MerbuzPixel** is an improved version of the **neopixel** library, which is available in MicroPython by default. A 16x16 matrix was tested on a **Wemos Mini d1 r1** microcontroller.

## How it use?

Just **download the library file** and import it into your board!

## Code

Example of using the library

```python
from merbuzpixel import *

merbuz = MerbuzPixel(pin=4, width=16, height=16) # Create class. first - pin of matrix, second - width of matrix, third - height

merbuz.setBrightness(3) # Set brightness 0-255

merbuz.setPixel(index=0, rgb=(255, 255, 255)) # Set pixel, first - index, second - tuple of RGB

merbuz.clearMatrix() # Just clear matrix. All

merbuz.fillPixels(firstIndex=6, secondIndex=70, rgb=(255, 255, 255)) # Fill by index led. First - index of first led, second - index of second led, third - tuple of RGB

merbuz.fillBackground(rgb=MerbuzPixel.PINK) # Fill all matrix. Use rgb as a argument

merbuz.clearPixel(index=0) # Pixel index to clear
```





