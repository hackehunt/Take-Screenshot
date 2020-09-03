from PIL import Image, ImageGrab
import time

def takeshot():
    image = ImageGrab.grab()
    image.show()

if __name__ == "__main__":
    time.sleep(2)
    takeshot()