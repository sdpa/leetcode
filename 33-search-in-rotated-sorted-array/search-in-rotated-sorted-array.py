class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotated = False
        if nums[0] > nums[-1]:
            rotated = True

        if rotated:
            k = -1
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else: 
                    right = mid
            k = left
            
            if target >= nums[0] and k != 0:
                return self.binarySearch(0, k-1, nums, target)
            else:
                return self.binarySearch(k, len(nums) -1, nums, target)

        else:
            # binary search
            return self.binarySearch(0, len(nums) - 1, nums, target)

    def binarySearch(self, left, right, nums, target):
        while left <= right:
            mid_idx = left + (right - left) // 2
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                left = mid_idx + 1
            else:
                right = mid_idx - 1
        return -1


