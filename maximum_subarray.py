def max_subarray(arr):
    max_sub_arr = local = arr[0]
    for i in range(0,len(arr)):
        local = arr[i]
        for j in range(i+1,len(arr)):
            local = local + arr[j]
            if local > max_sub_arr:
                max_sub_arr = local
                max_arr = arr[i:j+1]
    return max_sub_arr, max_arr

a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(max_subarray(a))

                