class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # first find element closest to k and then it will be i+k elements from that. 
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
        