class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(a, b):
            if a + b > b + a:
                return -1  # a should come first
            elif a + b < b + a:
                return 1   # b should come first
            else:
                return 0

        array = list(map(str, nums))
        array.sort(key=cmp_to_key(compare))

        if array[0] == "0":
            return "0"
        largest = ''.join(array)

        return largest

        