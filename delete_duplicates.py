def deleteDuplicates(arr):
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
    return unique


arr = [1,3,4,5,1,2,2,3,3,5]
print('before deleting duplicates : ', arr)
new_arr = deleteDuplicates(arr)
print('after deleting duplicates : ', new_arr)