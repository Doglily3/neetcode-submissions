class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                                    # 存还没被关闭的开括号
        matching = {')': '(', ']': '[', '}': '{'}    # 每个闭括号对应的开括号

        for c in s:
            if c in '([{':          # 是开括号
                stack.append(c)     # 压入栈
            else:                   # 是闭括号
                if not stack:       # 栈是空的，没有可以匹配的开括号
                    return False
                if stack[-1] != matching[c]:   # 栈顶的开括号跟当前闭括号不匹配
                    return False
                stack.pop()         # 匹配成功，把栈顶弹出

        return len(stack) == 0      # 最后栈为空才说明全部匹配完了