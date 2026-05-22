from datetime import datetime

from image_to_code import image_to_code


def decrypt(s):
    arr = image_to_code(len(s))

    chars = [ord(c) for c in s]


    for line in arr:
        for i in range(len(chars)):
            pixel = int(line[i % len(line)][0])
            if chars[i] > 120:
                chars[i] = chars[i] - pixel
            elif chars[i] < 0:
                chars[i] = chars[i] + pixel
            else:
                chars[i] = chars[i] + pixel + int(datetime.now().strftime("%M"))

    for i in range(len(chars)):
        chars[i] = int(chars[i]) % 256

    result = ''.join(chr(c) for c in chars)

    return result

