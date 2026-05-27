import random
import time

from PIL import Image
import numpy as np

def image_to_code(length, nums):
    img = Image.open('baseimg.jpg')

    img = img.resize((length*2, length*2))

    n = (time.time_ns()%10000)//1000

    if n <=4:
        nums[0] = 0
    else:
        nums[0] = 1

    if n%2 == 0 :
        nums[1] = 0
    else:
        nums[1] = 1

    box = (((length-1)*nums[0]), (length-1)*nums[1], (length-1)*(nums[0]+1), (length-1)*(nums[1]+1))

    img = img.crop(box)

    pixels = np.array(img)
    pixels = np.where(pixels > 128, pixels // 2, pixels)

    return pixels

def get_specific_area(length, nums):
    img = Image.open('baseimg.jpg')

    img = img.resize((length * 2, length * 2))

    box = ((length - 1) * nums[0], (length - 1) * nums[1], (length - 1) * (nums[0] + 1), (length - 1) * (nums[1] + 1))

    img = img.crop(box)

    pixels = np.array(img)
    pixels = np.where(pixels > 128, pixels // 2, pixels)

    return pixels
