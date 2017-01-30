# Find the largest element of the array


def largest_number(lst):
    max_number = lst[0]
    for elem in lst:
        if elem > max_number:
            max_number = elem
    return max_number

a = [1, 3, 4, 3, 8, 2]
print(largest_number(a))