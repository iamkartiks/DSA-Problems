def bubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

a = [0,2,4,6,3,8,1,3,8,6]
bubbleSort(a)
print(a)