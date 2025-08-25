def binary_search(arr, target):
    len_arr = len(arr)
    low=0
    high=len_arr-1
    mid= int (low + ((high-low)/2))

    while low<=high:

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low=mid+1
            mid= int (low + ((high-low)/2))
        else:
            high=mid-1
            mid= int (low + ((high-low)/2))
    return -1 #if no target present
arr=[2]
target=22
index=binary_search(arr, target)
print(index)
