    while low<=high:
        mid= low+ (high-low)//2
        if arr[mid]==target:
            set_index=mid
            #checking at left side mid-1 to low
            for i in range(mid, low-1, -1):
                if arr[i] == target:
                    set_index = i
            return set_index
        elif arr[mid]<target:
            low= mid+1
        else:
            high=mid-1
    return -1

arr=[1,2,2,2,3,3,4,4,4,4,5,6]
target=3
first= first_index(arr, target)
print(first)
                                                                                                                                                22,4          Bot
