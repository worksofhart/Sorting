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
        middle = (high + low) // 2
        element = arr[middle]

        if element < target:
            low = middle + 1
        elif element > target:
            high = middle - 1
        else:
            return middle

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    if len(arr) == 0 or high < low:
        return -1  # array empty or no match found

    middle = (low+high)//2
    element = arr[middle]

    if element > target:
        return binary_search_recursive(arr, target, low, middle - 1)
    elif element < target:
        return binary_search_recursive(arr, target, middle + 1, high)
    else:
        return middle
