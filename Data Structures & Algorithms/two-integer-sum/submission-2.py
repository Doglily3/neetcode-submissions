class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, x in enumerate(nums):
            left = target - x
            if left not in hashmap:
                hashmap[x] = i
            else:
                return [hashmap[left], i]