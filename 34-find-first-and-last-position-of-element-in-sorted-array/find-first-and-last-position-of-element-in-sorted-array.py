class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        # Position of a target value. 

        def search(nums, target, leftBias):
            left = 0
            right = len(nums) - 1
            i = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target: # target is in the right section
                    left = mid + 1
                elif nums[mid] > target: # Target is in the left section
                    right = mid - 1
                else:
                    i = mid
                    # Find the left and right. 
                    # Edge case. go to left until nums[i] and nums[i+1] and 
                    if leftBias:
                        right = mid - 1
                    else:
                        left = mid + 1
            return i

        left = search(nums, target, True)
        right = search(nums, target, False)

        return [left, right]

            


        