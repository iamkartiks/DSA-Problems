# APPLICATION OF COUNTING SORT 

def numbersInrange(arr,interval):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_ele = max_element-min_element+1

    count = [0 for _ in range(range_of_ele)]

    for i in range(len(arr)):
        count[arr[i]-min_element] += 1
    
    for i in range(1,len(count)):
        count[i] += count[i-1]
    
    # print(count)

    nos = count[6]-count[0]

    return nos

arr =  [9,8,8,6,5,4,3,1,0]
period = [1,6]
print(numbersInrange(arr,period))


    