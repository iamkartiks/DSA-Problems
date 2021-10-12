def inversion(arr):
    l=[]
    count = 0
    for i in range(0,len(arr)):
        for j in range(1,len(arr)):
            if i<j and arr[i]>arr[j]:
                count+=1
                l.append((arr[i],arr[j]))
    return count,l

a = [2,3,8,6,1]
print(inversion(a))
