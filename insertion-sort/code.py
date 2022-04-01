import random

### Insertion sort in python ###
a = random.sample(range(10, 30), 10)


def insertion_sort_a(a):  # Ascending
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a


def insertion_sort_d(a):  # Descending
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a
