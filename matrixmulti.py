def matrixmulti(arr1,arr2):
    res =  [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
    for i in range(0,len(arr1)):
        for j in range(0, len(arr2[0])):
            for k in range(0, len(arr1)):
                res[i][j] += arr1[i][k]*arr2[k][j]
    return res

A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

print(matrixmulti(A,B))