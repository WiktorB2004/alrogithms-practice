import random

array = [2, 4, 30, 200, 700, 1230, 93912039, 129902109000]


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


if __name__ == "__main__":
    print(binary_search(array, 0, len(array) - 1, 700))
