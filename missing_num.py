def find_missing_number(arr):
    n = len(arr) + 1
    total_xor = 0
    for i in range(1, n + 1):
        total_xor ^= i
        print('xor value', total_xor)    
    print(total_xor)
    arr_xor = 0
    for num in arr:
        arr_xor ^= num
        print('arr_xor', arr_xor)
    missing_number = total_xor ^ arr_xor
    return missing_number

# Example usage
array = [1, 2, 4, 5, 6, 7, 8, 9, 10]  # Array with missing number 3
missing_num = find_missing_number(array)
print("Missing number:", missing_num)
