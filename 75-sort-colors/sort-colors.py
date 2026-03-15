class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        mid = 0
        right = len(nums) - 1
        # Basically parition the list into 3 sets. 

        # Left -> 0s, middle - 1s, right - 2s. 

        while(mid <= right):
            if nums[mid] == 0:
                # Swap with left and increment left. 
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
        

                

        
        