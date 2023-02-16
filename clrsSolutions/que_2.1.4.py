def search(x,arr):
    for i in range(0,len(arr)):
        if x == arr[i]:
            return i
        
    return None


arr = [1,2,3,4,5,67]
x = 4

print(search(4,arr))