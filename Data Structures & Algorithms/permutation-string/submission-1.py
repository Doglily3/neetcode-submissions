class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        window = {}
        need = {}

        for i in range(len(s1)):
            need[s1[i]] = need.get(s1[i],0) + 1

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right],0) + 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if  window[s2[left]] == 0:
                    del window[s2[left]]
                
                left += 1
            if right - left + 1 == len(s1):
                if window == need:
                    return True
                
        return False