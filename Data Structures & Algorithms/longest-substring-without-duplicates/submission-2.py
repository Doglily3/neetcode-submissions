class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setchar = set()
        maxlen = 0
        left = 0
        for i in range(len(s)):
            while s[i] in setchar:
                setchar.remove(s[left])
                left+=1
            
            setchar.add(s[i])
            maxlen = max(maxlen, i-left+1)

        return maxlen
