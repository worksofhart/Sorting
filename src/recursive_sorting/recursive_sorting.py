
def merge(arrA, arrB):
    lenA, lenB = len(arrA), len(arrB)
    # Initialize a list large enough to hold both sorted lists
    merged_arr = [0] * (lenA + lenB)

    # Build a merged list, stepping through arrA and arrB
    # and adding the lowest values in order, until the end
    # of either list is reached
    indexA = indexB = merged_index = 0
    while indexA < lenA and indexB < lenB:
        if arrA[indexA] <= arrB[indexB]:
            merged_arr[merged_index] = arrA[indexA]
            indexA += 1
        else:
            merged_arr[merged_index] = arrB[indexB]
            indexB += 1
        merged_index += 1

    # Add the remaining elements from whichever list hadn't
    # been stepped through completely
    if indexA < lenA:
        merged_arr[merged_index:] = arrA[indexA:]
    else:
        merged_arr[merged_index:] = arrB[indexB:]

    return merged_arr


def merge_sort(arr):
    lenArr = len(arr)
    # While the data set contains more than one item, split it in half
    # Once down to a single element, you have also *sorted* that element
    if lenArr > 1:
        half = lenArr // 2
        # Start merging sorted lists together into larger, sorted sets
        return merge(merge_sort(arr[:half]), merge_sort(arr[half:lenArr]))

    return arr

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    right_start = mid + 1
    if arr[mid] <= arr[right_start]:
        return

    while start <= mid and right_start <= end:
        # Merge in place by removing lower values from the right portion
        # and inserting them into the correct place in the left
        if arr[start] <= arr[right_start]:
            start += 1
        else:
            element = arr.pop(right_start)
            arr.insert(start, element)
            start += 1
            mid += 1
            right_start += 1

    return arr


def merge_sort_in_place(arr, l, r):
    if (l < r):
        # While the data set contains more than one item, split it in half
        # Once down to a single element, you have also *sorted* that element
        mid = (l + r) // 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid+1, r)
        # Start merging sorted lists together into larger, sorted sets
        merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
