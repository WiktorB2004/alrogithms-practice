import random
array = [random.randint(1,1000) for x in range(1,200)]
## Selection sort algorithm ##
def selection_sort(array):
    for i in range(len(array)):
        swap_i = i
        swap_value = array[i]
        step = i + 1
        for j in range(step, len(array)):
            if swap_value > array[j]:
                swap_i = j
                swap_value = array[j]
        temp = array[i]
        array[i] = swap_value
        array[swap_i] = temp
    return array

if __name__ == '__main__':
    print(selection_sort(array))