import random

### LINEAR SEARCH ALGORITHM ###
a = [random.randint(1, 10) for x in range(10)]
v = 2

# Find the index of v
def linear_search(a):
    for i in range(len(a)):
        if a[i] == v:
            return i
    return None
