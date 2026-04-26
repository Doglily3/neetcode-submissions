class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for x in tokens:
            if x.lstrip("-").isnumeric():
                stack.append(int(x))
                continue
            
            if x == "+":
                b = stack.pop()
                a = stack.pop()
                c = a + b
                stack.append(c)

            elif x =="-":
                b = stack.pop()
                a = stack.pop()
                c = a - b
                stack.append(c)

            elif x =="*":
                b = stack.pop()
                a = stack.pop()
                c = a * b
                stack.append(c)
            
            else:
                b = stack.pop()
                a = stack.pop()
                c = int(a / b)
                stack.append(c)
        return int(stack.pop())