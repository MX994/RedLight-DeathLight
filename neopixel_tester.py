import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 256, brightness=0.1, auto_write=False)
pixels.fill((0, 255, 0))
pixels.show()