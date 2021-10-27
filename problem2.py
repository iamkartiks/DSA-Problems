#BIT WISE OPERATION PAIRS

def solve(X,Y,A,B):
    count=0
    for i in range(len(A)):
        for j in range(len(B)):
                if(A[i]^B[j])&X == (A[i]^B[j])&Y:
                    count+=1
    return count


print(solve(5,4,[2,4,6],[3,5,6]))