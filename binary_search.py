def binary_search(arr,l,h,target):
    if h>=l:
        mid = l+(h-l)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            return binary_search(arr,mid+1,h,target)
        elif arr[mid]>target:
            return binary_search(arr,l,mid-1,target)
    else:
        return -1

a = [1,43,6,8,9,885]
target = 8

print(binary_search(a,0,len(a)-1,target))