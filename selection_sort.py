def selection_sort(array):
    for i in range(len(array)):
        # Assume the first element is the smallest
        smallest_el_index = i
        # Search for smallest element in the remaining unsorted elements and update smallest_el_index if found
        for j in range(i+1, len(array)):
            if array[j] < array[smallest_el_index]:
                smallest_el_index = j
        
        # Swap elements positions - move the smallest element to the beginning of the array
        array[i], array[smallest_el_index] = array[smallest_el_index], array[i]
    
    return array
    
array = [4, 65, 2, -31, 6]
print(selection_sort(array)) 
