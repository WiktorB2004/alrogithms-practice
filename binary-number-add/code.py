import random

### Binary number adding algorithm

num1 = "".join([str(random.randint(0, 1)) for x in range(8)])
num2 = "".join([str(random.randint(0, 1)) for x in range(8)])


def add_binary_numbers(a, b):
    carry = 0
    result = ""
    for i in range(7, -1, -1):
        r = carry
        r += 1 if a[i] == "1" else 0
        r += 1 if b[i] == "1" else 0
        result = ("1" if r % 2 == 1 else "0") + result

        carry = 0 if r < 2 else 1

    if carry != 0:
        result = "1" + result

    return result


print(add_binary_numbers(num1, num2))
