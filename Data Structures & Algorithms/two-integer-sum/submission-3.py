class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in hashmap:
                return [hashmap[diff],i]
            else:
                hashmap[x] = i
        return []