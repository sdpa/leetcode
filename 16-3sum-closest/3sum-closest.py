class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # Sort these numbers. 
        # Fix the 3rd number. 


        # For each 3rd number, find the other 2 where their total sum is closes. i.e. abs(sum(i + j + k) - target)) is min

        diff = float('inf')
        closes = 0
        nums.sort()

        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1
            while(i < j):
                cur_sum = nums[k] + nums[i] + nums[j]
                if cur_sum < target: # We need to add a bigger number for i.
                    i += 1
                elif cur_sum > target:
                    j -= 1
                else:
                    return cur_sum
                if abs(cur_sum - target) < diff:
                        closest = cur_sum
                        diff = abs(cur_sum - target) 
        return closest


        