class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        max_count = 0
        for num in num_set:
            if (num - 1) not in num_set:
                start = num
                count = 0
                while(start in num_set):
                    start += 1
                    count += 1
                max_count = max(count, max_count)
        
        return max_count
            

            



        