class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        left = 0

        for right in range(len(s2)):
            # 把右边字符放进窗口
            c = s2[right]
            window[c] = window.get(c, 0) + 1
            
            # 如果窗口太大，就缩小左边
            if right - left + 1 > len(s1):
                left_char = s2[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1

            # 如果窗口长度刚好等于 len(s1)，就比较
            if right - left + 1 == len(s1):
                if window == need:
                    return True

        return False