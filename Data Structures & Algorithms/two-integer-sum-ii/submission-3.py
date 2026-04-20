class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i<j:
            if numbers[j] > target:
                j -=1
                continue
            val = numbers[i] + numbers[j]

            if val>target:
                j-=1
                continue

            if val<target:
                i+=1
                continue
            if val == target:
                return [i+1,j+1]
        return [0]