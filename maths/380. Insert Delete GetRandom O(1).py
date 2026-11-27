import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        self.index_map[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        idx = self.index_map[val]
        last = self.nums[-1]

        self.nums[idx] = last
        self.index_map[last] = idx

        self.nums.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)