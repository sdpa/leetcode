class Solution:
    def findMin(self, nums: List[int]) -> int:
        result=float('inf')
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2 
            if nums[low]<=nums[mid]:
                if nums[low]<result:
                    result=nums[low] 
                low=mid+1 
            elif nums[mid]<nums[high]:
                if nums[mid]<result:
                    result=nums[mid]
                high=mid-1 
        return result
            
            
