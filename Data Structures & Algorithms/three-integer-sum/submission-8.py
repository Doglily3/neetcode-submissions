class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start = i+1
            end = len(nums)-1

            target = -1 * nums[i]

            while start<end:
                val = nums[start]+nums[end]
                if val>target:
                    end-=1
                elif val<target:
                    start+=1
                else:
                    result.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1

                    while start<end and nums[start] == nums[start - 1]:
                        start +=1
                    while start<end and nums[end] == nums[end + 1]:
                        end -=1
                
        return result
