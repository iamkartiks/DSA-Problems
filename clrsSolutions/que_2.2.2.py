def selection_sort(arr):    
    for i in range(0,len(arr)):
        key_index = i
        j = i+1
        while j < len(arr) and arr[j] < arr[key_index]:
            key_index = j
            j += 1
        arr[key_index],arr[i] = arr[i], arr[key_index]

    return arr



if __name__ == "__main__":
    unsorted_array = [3,2,1,5,50,44]
    print(selection_sort(unsorted_array))