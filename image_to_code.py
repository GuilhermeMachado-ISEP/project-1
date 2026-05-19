from PIL import Image
import numpy as np

def image_to_code():
    img = Image.open('paint.png')

    img = img.convert('L')

    pixels = np.array(img)

    return pixels
