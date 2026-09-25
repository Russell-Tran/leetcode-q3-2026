class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pairs = {}
        for i, num in enumerate(nums):
            if num in pairs:
                return [i, pairs[num]]
            value = target - num
            pairs[value] = i
            

"""
value = 6 - 3 = 3
pairs[3] = 0
if 3
"""