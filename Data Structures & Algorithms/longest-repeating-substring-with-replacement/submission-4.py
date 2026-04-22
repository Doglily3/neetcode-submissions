class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = {}
        maxf = 0
        maxlength = 0
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i],0)+1
            maxf = max(maxf, hashmap[s[i]])

            while i - left + 1 - maxf > k:
                hashmap[s[left]] -= 1
                left += 1

            maxlength = max(maxlength, i - left + 1)
        
        return maxlength