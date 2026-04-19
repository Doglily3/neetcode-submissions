class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nonduplicate = set(nums)
        if len(nums) != len(nonduplicate):
            return True
        return False
