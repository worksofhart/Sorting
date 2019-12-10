
def selection_sort(arr):
    # Loop through the elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # - For all indices EXCEPT the last index:
        # Loop through elements on right-hand-side of current index and find the smallest element
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # Swap the element at current index with the smallest element found in above loop
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


def bubble_sort(arr):
    swaps = True
    while swaps:
        swaps = False
        # - Loop through the array
        for i in range(1, len(arr)):
            # Compare each element to its neighbor
            # If elements in wrong position, swap them
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swaps = True
    # If swaps were performed, the loop repeats

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
