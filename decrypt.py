from math import floor

from image_to_code import get_specific_area


def decrypt(s):

    chars = [ord(c) for c in s]

    nums = [int(s[-2]), int(s[-1])]

    arr = get_specific_area(len(chars)-2, nums)

    for line in arr:
        for i in range(len(chars)-2):
            if i%3==0:
                chars[i] = chars[i] - line[i%len(line)][0]
            elif i%3==1:
                chars[i] = chars[i] + line[i%len(line)][1]
            else:
                chars[i] = chars[i] - line[i%len(line)][2]

    for i in range(len(chars)-2):
        if chars[i] < 0:
            while chars[i] < 0:
                chars[i] = chars[i] + 127
        elif chars[i] > 127:
            while chars[i] > 127:
                chars[i] = chars[i] - 127
        chars[i] = floor(chars[i])

    result = ''.join(chr(c) for c in chars)

    return result[:-2]

