def partition(A,p,r):
    pivot=A[r-1]
    i = p-1
    for j in range(p,r):
        if A[j]>pivot:
            i=i+1
            A[j],A[i]=A[i],A[j]
    A[i+1],A[r-1]=A[r-1],A[i+1]
    return i+1

def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

arr = [3,2,6,2,0,88,5,4]
quicksort(arr,0,len(arr))
print(arr)

'''
Randomized quicksort basically pick any random index number between low-high, and change the pivot elemnt with arr[random _index]
and then apply partition algorithm on it....
'''


# HOARE PARTITION ....

'''
Hoare_Partition(A,p,r):
    x = A[p]
    i = p-1
    j = r+1
    while True:
        repeat:
            j=j-1
        until A[j]<=x

        repeat:
            i=i+1
        until A[i]>=x
        if i<j:
            exchange A[i] with A[j]
        else:
            return j

'''
