arr = [1, 2, 3]

def sum_array(arr):
    # define base case 
    if len(arr) == 0:
        return 0
    # define recursive case - sum array first element and the rest of the array till the last element. do it till the base case is reached
    else: 
        return arr[0] + sum_array(arr[1:])

print(sum_array(arr))  

def count_arr_elements(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_arr_elements(arr[1:])
    
# print(count_arr_elements(arr))

