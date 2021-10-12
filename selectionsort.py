def selectionSort(arr):
    for i in range(0,len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr

a = [0,5,3,8,1,9,3,2,7]
selectionSort(a)
print(a)