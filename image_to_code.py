import random
import time
from datetime import datetime

from PIL import Image
import numpy as np

def image_to_code(length):
    img = Image.open('imagh.jpg')

    img = img.resize((length, 40))

    img = img.convert()

    pixels = np.array(img)
    pixels = np.where(pixels > 128, pixels/2, pixels)

    return pixels