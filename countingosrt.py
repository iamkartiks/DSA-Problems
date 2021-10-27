def counting_sort(A):
    range_of_ele = int(max(A))-int(min(A))+1
    c = [0 for _ in range(range_of_ele)]
    b = [0 for _ in range(len(A))]

    for i in range(len(A)):
        c[A[i]-int(min(A))] += 1
    # print(c)
    for i in range(1,len(c)):
        c[i] += c[i-1]
    
    # print(c)
    for i in range(len(A)-1,-1,-1):
        b[c[A[i]-int(min(A))]-1]=A[i]
        c[A[i]-int(min(A))] -= 1
    
    for i in range(len(A)):
        A[i]=b[i]
    

arr = [9,3,4,1,8,5,6,0,8]
counting_sort(arr)
print(arr)