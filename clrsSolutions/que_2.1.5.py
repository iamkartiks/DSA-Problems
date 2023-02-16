def binary_addition(A, B):
    n = len(A)
    C = [0] * (n + 1)
    carry = 0
    for i in range(n-1, 0, -1):
        sum = A[i] + B[i] + carry
        C[i + 1] = sum % 2
        carry = sum // 2
    C[0] = carry
    return C




if __name__ == "__main__":
    x = [1,0,1,0,1,0]
    y = [1,1,1,1,1,0]
    print(binary_addition(x,y))