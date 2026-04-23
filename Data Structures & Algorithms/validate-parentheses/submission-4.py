class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {"]":"[", ")":"(", "}":"{"}
        stack = []

        for x in s:
            if x in "([{":
                stack.append(x)
            else:
                if not stack or hashmap[x] != stack[-1]:
                    return False
                    
                stack.pop()
        
        return len(stack) == 0
