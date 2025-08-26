class Solution(object):
   def searchInsert(self,arr, target):
    low, high=0, len(arr)-1
    if target < arr[low]:
        return 0
    elif target>arr[high]:
        return high+1
    else: # either target present or need to insert between
        while low<=high:
            mid=low+(high-low)//2
            if target== arr[mid]:
                return mid
            elif target< arr[mid]:
                high=mid-1
            else:
                low=mid+1
        # print(low,mid,high)
        if target < arr[mid]:
            return mid
        else:
            return mid+1     
