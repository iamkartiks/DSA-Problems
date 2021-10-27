# HEAP MINIMUM :- return A[0] of min-heap

# EXTARCT MIN :- 
'''
def heapify(A,n,i):
    smallest = i
    l = 2*i+1
    r = 2*i+2

    if l<n and A[l]<A[i]:
        smallest = l
    
    if r<n and A[r]<A[smallest]:
        smallest=r
    
    if smallest != i:
        A[smallest],A[i]=A[i],A[smallest]
        heapify(A,n,i)

def heap_minimum(A):
    n =len(A)
    heapify(n//2-1,-1,-1)

def extract_min(A):
    n=len(A)-1
    if len(A)<1:
        print("underflow")
    else:
        for i in range(n,-1,-1):
            heapify(A,n,0)
        min = A[0]
    return min

print(extract_min([2,0,5,6,4,9]))

'''

## HEAP USING LINKED LISTS MIGHT HELP......