class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        maxf = 0
        maxlength = 0
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            maxf = max(maxf, hashmap[s[right]])

            while right - left + 1 - maxf > k:
                hashmap[s[left]] -= 1
                left += 1

            maxlength = max(maxlength, right-left + 1)

        return maxlength
