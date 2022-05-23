# Rearrange array such that arr[i] = i
def rearrange_1(arr):
    res = []
    for i in range(len(arr)):
        if i in arr:
            res.append(i)
        else:
            res.append(-1)
    return res


# Rearrange array such that elements at even positions are greater than all elements before it and elements at odd positions are less than all elements before it.
def rearrange_2(arr):
    pass


if __name__ == "__main__":
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    out1 = rearrange_1(arr)
    out2 = rearrange_2(arr)
    print(
        "arr[i] = i {}, \narr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i: {}".format(
            out1, out2
        )
    )
