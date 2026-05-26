import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

from image_to_code import image_to_code


def encrypt(s):
    nums = [0, 0]

    arr = image_to_code(len(s), nums)

    chars = [ord(c) for c in s]


    for line in arr:
        for i in range(len(chars)):
            if i%3==0:
                chars[i] = chars[i] + line[i%len(line)][0]
            elif i%3==1:
                chars[i] = chars[i] - line[i%len(line)][1]
            else:
                chars[i] = chars[i] + line[i%len(line)][2]


    for i in range(len(chars)):
        chars[i] = int(chars[i]) % 128

    result = ''.join(chr(c) for c in chars)

    result += str(nums[0]) + str(nums[1])

    return result

