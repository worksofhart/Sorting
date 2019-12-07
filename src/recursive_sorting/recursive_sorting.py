# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    lenA, lenB = len(arrA), len(arrB)
    elements = lenA + lenB
    merged_arr = [0] * elements
    # TO-DO
    
    i = j = k = 0
    while i < lenA and j < lenB:
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    
    while i < lenA:
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
     
    while j < lenB:
        merged_arr[k] = arrB[j]
        j += 1
        k += 1
        
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
# Algorithm
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
def merge_sort(arr):
    # TO-DO
    lenArr = len(arr)
    if lenArr > 1:
        half = lenArr // 2
        # print(f"mergesort({arr[:half]}, {arr[half:lenArr]})")
        return merge(merge_sort(arr[:half]), merge_sort(arr[half:lenArr]))
        
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
