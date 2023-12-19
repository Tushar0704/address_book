# This function does a binary search on a given sorted csv file.
def binary_search(arr, low, high, x, key=4):

    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if int(arr[mid].strip().split(',')[key]) == int(x):
            return arr[mid]
 
        # If element is smaller than mid, then it can only
        # be present in left sub array
        elif int(arr[mid].strip().split(',')[key]) > int(x):
            return binary_search(arr, low, mid - 1, x, key)
 
        # Else the element can only be present in right sub array
        else:
            return binary_search(arr, mid + 1, high, x, key) 
    else:
        # Element is not present in the array
        return -1
