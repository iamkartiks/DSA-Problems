'''
Python program for bubble sort


Bubble Sort :

In this sort we start the iterations from the first element and picking elements in pair and replacing them according 
to their suitable position.
'''

def bubbleSort(arr):
    '''
    Arguments : input unsorted array
    Returns : Sorted Array
    '''
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

a = [0,2,4,6,3,8,1,3,8,6]
bubbleSort(a)
print(a)