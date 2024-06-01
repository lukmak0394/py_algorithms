arr = [3, 22, 8, -5, 7, 4, 12]

# def quicksort(arr):
#     # base case
#     if len(arr) <= 1:
#         return arr
#     else:
#         # define pivot as the first element of the array
#         pivot = arr[0]
#         # elements smaller than pivot
#         less = [i for i in arr[1:] if i <= pivot]
#         # elements greater than pivot
#         greater = [i for i in arr[1:] if i > pivot]
        
#         return quicksort(less) + [pivot] + quicksort(greater)


# Lomuto partition scheme  
def quicksort(arr, start, end):
    # base case
    if start <= end:
        pivot_index = partition(arr, start, end)    
        # elements smaller than pivot
        quicksort(arr, start, pivot_index-1)
        # elements greater than pivot
        quicksort(arr, pivot_index+1, end)
    return arr

''' Function to partition the array into two parts - it will put all elements less than or equal to pivot on the left side of the pivot
and all elements greater than pivot on the right side of the pivot.'''
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    # Iterate through the array and compare each element with the pivot. Move smaller elements to the beginning of the array
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    # Swap pivot with the element at index i
    arr[i], arr[end] = arr[end], arr[i]
    return i

print(quicksort(arr, 0, len(arr)-1))  
