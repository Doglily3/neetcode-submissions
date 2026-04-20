class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_a = sorted(s)
        d_a = sorted(t)

        if s_a != t_a:
            return False
        return True