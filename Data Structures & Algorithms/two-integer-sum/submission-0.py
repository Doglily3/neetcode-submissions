class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, x in enumerate(nums):
            left = target - x
            if left in hashmap:
                return [hashmap[left], i]

            hashmap[x] = i