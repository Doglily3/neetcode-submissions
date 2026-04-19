class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        front = 1
        for i in range(len(nums)):
            result[i] = front
            front = front * nums[i]
        
        back = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = back * result[i]
            back = nums[i] * back

        return result