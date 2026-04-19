class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        hashmap = 1
        for i in range(len(nums)):
            result[i] = hashmap
            hashmap *= nums[i]
        
        back = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= back
            back *= nums[i]
        
        return result
            