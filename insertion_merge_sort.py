def insertion_sort(unsorted_array):
    n = len(unsorted_array)
    
    for i in range(1,n):
        key = unsorted_array[i]
        j = i - 1
        while j > -1 and key < unsorted_array[j]:
            # if k
                unsorted_array[j+1] = unsorted_array[j]
                j = j - 1 
        unsorted_array[j+1] = key

    return unsorted_array 



def merge_sort():
    pass





unsorted_array = [2,4,1,0,44,23,11]

print(insertion_sort(unsorted_array))