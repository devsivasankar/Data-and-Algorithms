# linear search in array
arr = [1,2,3,4,5,6,7,8,9,10]

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return 'not available'

x = linear_search(arr,1)
print(x)