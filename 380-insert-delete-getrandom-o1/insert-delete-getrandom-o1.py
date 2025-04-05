import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.map = {}

    def insert(self, val: int) -> bool:
        # Add element to the last
        if val in self.map:
            return False

        self.nums.append(val)
        self.map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        # Get the index of the element. switch with last element 
        if val in self.map:
            i = self.map[val]

            # update the index of arr[-1] to the new index.
            self.map[self.nums[-1]] = i

            self.nums[i] = self.nums[-1]

            self.map.pop(val)
            self.nums.pop()

            return True
        return False

    def getRandom(self) -> int:
        # print(self.nums)
        return random.choice(self.nums)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()