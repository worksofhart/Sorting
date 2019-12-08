# STRETCH: implement Linear Search
def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (high + low) // 2
        element = arr[mid]

        if element < target:
            low = mid + 1
        elif element > target:
            high = mid - 1
        else:
            return mid

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
