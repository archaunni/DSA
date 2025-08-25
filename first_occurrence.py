def first_index(arr, target):
    len_arr = len(arr)
    low, high = 0, len_arr - 1
    set_index=-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            set_index = mid
            high = mid-1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return set_index

arr=[1,2,2,2,3,3,4,4,4,4,5,6]
target=4
first= first_index(arr, target)
print(first)
