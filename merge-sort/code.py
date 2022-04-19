import random

array = [random.randint(-100, 100) for x in range(10)]


def merge_sort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        leftArr = arr[:r]
        rightArr = arr[r:]

        merge_sort(leftArr)
        merge_sort(rightArr)

        i = j = k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1


if __name__ == "__main__":
    merge_sort(array)
    print(array)
