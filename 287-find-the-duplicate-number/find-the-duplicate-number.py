class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Perform swapping of nums, and the moment you find a num that is alreay swapped. return that. 


        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                target_idx = nums[i] - 1
                if nums[i] == nums[target_idx]:
                    return nums[i]
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
            else:
                i += 1
            
            
        