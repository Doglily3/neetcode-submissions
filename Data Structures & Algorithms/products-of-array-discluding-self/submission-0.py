class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if i == 0:
                hashmap[i] = 1
            else:
                hashmap[i] = hashmap[i-1] * nums[i-1]
        i = len(nums)-1
        back = {}
        back[i] = 1
        i -= 1
        while i >= 0:
            back[i] = back[i+1]*nums[i+1]
            i -= 1
        result = []
        for i in range(len(nums)):
            result.append(hashmap[i]*back[i])
        
        return result
            