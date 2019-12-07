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
        merged_arr[k] = arrA[j]
        j += 1
        k += 1
        
    print(merged_arr)
    return merged_arr

# merge([0,2,4,6,8,10], [1,3,5,7,9])

# TO-DO: implement the Merge Sort function below USING RECURSION
# Algorithm
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
def merge_sort(arr):
    # TO-DO
    i = raw_input("Hit enter to continue")
    lenArr = len(arr)
    while lenArr > 1:
        half = lenArr // 2
        print(half, lenArr)
        merge(merge_sort(arr[:half]), merge_sort(arr[half:lenArr]))
        
    # print arr
    print "Returning array"
    return arr

merge_sort([1, 8, 2])

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
