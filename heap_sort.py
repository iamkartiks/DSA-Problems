def heapify(A,n,i):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and A[l]>A[i]:
        largest=l
    
    if r<n and A[r]>A[largest]:
        largest=r
    
    if largest !=i:
        A[i],A[largest]=A[largest],A[i]

        heapify(A,n,largest)

def buildmaxHeap(A):
    n=len(A)
    for i in range(n//2,-1,-1):
        heapify(A,n,i)

def heap_sort(A):
    buildmaxHeap(A)
    for i in range(len(A)-1,-1,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,i,0)

    return A[0]


arr = [1,0,9,5,8,3,11,4]
print(heap_sort(arr))
print(arr)