def quicksort(arr):
    # define base case
    if len(arr) <= 1:
        return arr
    else:
        # define pivot element
        pivot = arr[0]
        # define elements less than pivot and elements greater than pivot
        less = [i for i in arr[1:] if i <= pivot]
        # define elements greater than pivot
        greater = [i for i in arr[1:] if i > pivot]
        # return quicksort of elements less than pivot + pivot + quicksort of elements greater than pivot
        return quicksort(less) + [pivot] + quicksort(greater)
    

print(quicksort([3, 2, 8, 0, 12]))