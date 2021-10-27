# RECURSION ERROR NOT FOUND
def cross_sub_array(arr,low,mid,high):
    left_sum = -99999
    sum = 0 
    for i in range(mid,low-1,-1):
        sum = sum + arr[i]
        if sum>left_sum:
            left_sum=sum
            max_left = i
    
    right_sum = -99999
    sum = 0
    for i in range(mid+1,high):
        sum = sum + arr[i]
        if sum>right_sum:
            right_sum=sum
            max_right = i
    
    return (max_left,max_right,left_sum+right_sum)

def max_sub_arr(arr,low,high):
    if low==high:
        return (low,high,arr[low])


    mid = high+low// 2
    return   max(
        max_sub_arr(arr,low,mid),
        max_sub_arr(arr,mid+1,high),
        cross_sub_array(arr,low,mid,high)
    )


a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
low=0
high = len(a)-1
print(max_sub_arr(a,0,len(a)-1))