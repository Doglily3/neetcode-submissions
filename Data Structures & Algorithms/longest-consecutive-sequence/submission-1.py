class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set()

        for i in nums:
            num.add(i)
        maxlen = 0
        for x in num:
            if x-1 not in num:
                length = 1
                current = x
            while current + 1 in num:
                length += 1
                current+= 1
            maxlen = max(length, maxlen)
        return maxlen