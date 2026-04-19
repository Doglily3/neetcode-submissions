class Solution:

    def encode(self, strs: List[str]) -> str:
        length = ""
        output = ""
        for x in strs:
            length = str(len(x))
            output += length + ":"+ x 
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i 
            while s[j] != ":":
                j+=1 
            number = int(s[i:j])

            result.append(s[j+1:j+1+number])

            i = j+1+number

        return result