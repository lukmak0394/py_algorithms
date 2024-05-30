
# Binary search return position of given value in sorted array if it exists, otherwise return None
def binary_search(array, target):
    min = 0
    max = len(array) - 1

    # Loop until there's only one element left
    while min <= max:
        mid_index = (min + max) // 2
        guess = array[mid_index]
        if guess == target:
            return mid_index
        if guess < target:
            min = mid_index + 1
        else: 
            max = mid_index - 1

    return None


primes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = binary_search(primes, 5)
print(result)


