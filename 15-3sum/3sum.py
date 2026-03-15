class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        res = []
        for k in range(len(nums)-2):
            l = k + 1
            h = len(nums) - 1

            if k > 0 and nums[k] == nums[k-1]:
                continue

            while(l < h):
                if nums[l] + nums[h] < -nums[k] and l != k and h != k:
                    l += 1
                elif nums[l] + nums[h] > -nums[k] and l != k and h != k:
                    h -= 1
                elif nums[l] + nums[h] == -nums[k] and l != k and h != k:
                    res.append([nums[l], nums[h], nums[k]])

                    l += 1
                    h -= 1

                    while l < h and nums[l] == nums[l-1]:
                        l += 1
                    while l < h and nums[h] == nums[h+1]:
                        h -= 1
      
        return res


            

        


        