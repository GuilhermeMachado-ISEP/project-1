import datetime

from image_to_code import image_to_code


def encrypt(s):
    binary = image_to_code()

    n = int(datetime.datetime.now().strftime('%H%M%S'))

    print(n)

