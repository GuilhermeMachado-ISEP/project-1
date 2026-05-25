import random
from math import floor

from PIL import Image
import numpy as np

def image_to_code(length, nums):
    img = Image.open('imaghnaghtest.jpg')

    img = img.resize((length*2, length*2))

    img.show()

    nums[0] = random.randint(0,1)

    if nums[0] == 1:
        nums[1] = random.randint(1,2)
    else:
        nums[1] = random.randint(0,1)

    box = (((length-1)*nums[0]), (length-1)*nums[1], (length-1)*(nums[0]+1), (length-1)*(nums[1]+1))

    img = img.crop(box)

    pixels = np.array(img)
    pixels = np.where(pixels > 128, pixels/2, pixels)

    return pixels

def get_specific_area(length, nums):
    img = Image.open('imaghnaghtest.jpg')

    img = img.resize((length * 2, length * 2))

    img.show()

    box = ((length - 1) * nums[0], (length - 1) * nums[1], (length - 1) * (nums[0] + 1), (length - 1) * (nums[1] + 1))

    img = img.crop(box)

    pixels = np.array(img)
    pixels = np.where(pixels > 128, pixels / 2, pixels)

    return pixels
