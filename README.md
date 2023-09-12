# MerbuzPixel

**MerbuzPixel** is an improved version of the **neopixel** library. A 16x16 matrix was tested on a **Wemos Mini d1 r1** microcontroller.

## Contents
- [How it uses?](https://github.com/Merbuz/MerbuzPixel/tree/main#how-it-use)
  - [Using library](https://github.com/Merbuz/MerbuzPixel/tree/main#using-library)
  - [Class initialization](https://github.com/Merbuz/MerbuzPixel/tree/main#class-initialization)
  - [Functions](https://github.com/Merbuz/MerbuzPixel/tree/main#functions)
  - [Colors](https://github.com/Merbuz/MerbuzPixel/tree/main#colors)
- [Code example](https://github.com/Merbuz/MerbuzPixel/tree/main#code-example)

## How it use?

Just **download the library file** and import it into your board!

## Using library

Just import all from this library
```python
from merbuzpixel import *
```
Or import only what you need
```python
from merbuzpixel import MerbuzPixel
```

## Class initialization

```python
merbuz = MerbuzPixel(pin=4, width=16, height=16)
```
Create instance of class.
- `pin` pin connection to the matrix
- `width` width of matrix 
- `height` height of matrix

## Functions

**Control brightness of matrix**
```python
merbuz.setBrightness(brightness=3) 
```
- `brightness` brightness parameter 0-255

**Fill pixel in matrix**
```python
merbuz.setPixel(index=0, rgb=(255, 255, 255))
```
- `index` index of led in matrix
- `rgb` tuple with RGB code

**Clear all matrix. Does not require arguments**
```python
merbuz.clearMatrix() 
```

**Fill pixels in current range**
```python
merbuz.fillPixels(firstIndex=6, secondIndex=70, rgb=(255, 255, 255))
```
- `firstIndex` first index in range
- `secondIndex` last index in range
- `rgb` tuple with RGB code

**Fill background in matrix**
```python
merbuz.fillBackground(rgb=(255, 255, 255))
```
- `rgb` tuple with RGB code

**Clear pixel of selected index**
```python
merbuz.clearPixel(index=0)
```
- `index` index of pixel

**Draw any image to matrix! (16 on 16)**
```python
matrix.drawImage(file_name='place_your_file_name')
```
- `file_name` a file with an encoded image with the .merbuzpixel extension. You can get this file if you use the [MerbuzPixelImage](https://github.com/Merbuz/MerbuzPixelImage) library.

## Colors

**10 colors to choose from. You can use them instead of tuple RGB code:**
- `RED`
- `GREEN`
- `BLUE`
- `ORANGE`
- `YELLOW`
- `LIGHTBLUE`
- `WHITE`
- `VIOLET`
- `PURPLE`
- `PINK`

```python
MerbuzPixel.RED

MerbuzPixel.GREEN

MerbuzPixel.BLUE

MerbuzPixel.ORANGE

MerbuzPixel.YELLOW

MerbuzPixel.LIGHTBLUE

MerbuzPixel.WHITE

MerbuzPixel.VIOLET

MerbuzPixel.PURPLE

MerbuzPixel.PINK
```
Example of using color
```python
merbuz.fillBackground(rgb=MerbuzPixel.PINK)
```

## Code example

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

matrix.drawImage(file_name='place_your_file') # Drawing method
```





