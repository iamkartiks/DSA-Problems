# MAX AND MIN ON THE BASIS OF QUERY ARRAYS

def queries(A,query1,query2):
    temp = A
    for i in range(1,len(A)):
        temp[i]=1-max(temp[i],temp[i-1])
    for i in range(1,len(A)):
        A[i]=1-min(A[i],A[i-1])
    
    print(temp,A)
    r1=len(query1)-1
    r2 = len(query2)-1

    res=[]
    res.append(temp[r1])
    res.append(A[r2])

    return res
    
    

print(queries([0,0,0],[1,1,3],[2,1,3]))
