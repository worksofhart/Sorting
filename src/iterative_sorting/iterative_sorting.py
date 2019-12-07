# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
# Algorithm
# - Loop through your array
# - Compare each element to its neighbor
# - If elements in wrong position (relative to each other, swap them)
# - If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
def bubble_sort( arr ):
    swaps = True
    while swaps:
        swaps = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swaps = True    
                
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr