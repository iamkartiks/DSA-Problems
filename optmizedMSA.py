def max_sub_arr(arr):
    globalmax = localmax = arr[0]
    for i in range(1,len(arr)):
        localmax = max(arr[i], localmax+arr[i])
        if localmax>globalmax:
            globalmax = localmax
    return globalmax

a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(max_sub_arr(a))
