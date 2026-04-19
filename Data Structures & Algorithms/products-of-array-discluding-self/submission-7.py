class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
       
        front = 1
        for i in range(length):
            result[i] = front
            front = front * nums[i]

        back = 1
        for i in range(length-1, -1, -1):
            result[i] *= back
            back = back * nums[i]
        
        return result
