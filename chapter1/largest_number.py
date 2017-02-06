# Find the largest element of the array


def largest_number(lst):
    max_number = lst[0]  # O(1)
    for elem in lst:
        if elem > max_number:  # O(N)
            max_number = elem
    return max_number  # O(1)


a = [1, 3, 4, 3, 8, 2]
print(largest_number(a))
