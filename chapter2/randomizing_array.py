# This algorithm visits every position in the array once,
# so it has a run time of O(N), which should be fast enough for most applications.

import random


def randomizing_array(arr):
    max_i = len(arr)
    for index in range(0, max_i - 1):
        j = random.randint(0, max_i - 1)
        temp = arr[index]
        arr[index] = arr[j]
        arr[j] = temp
    print(arr)


test_arr = [1, 2, 3, 4, 5]

randomizing_array(test_arr)
