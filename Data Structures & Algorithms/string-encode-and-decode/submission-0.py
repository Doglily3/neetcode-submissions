class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for x in strs:
            encoded += (str(len(x)) + "#" + x)
        return encoded


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)   # 找到 # 的位置
            length = int(s[i:j])  # i 到 j 之间全是长度数字
            result.append(s[(j+1):(j+1+length)])
            i = j+1+length
        return result