from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for t in tokens:
            if t in operators:
                i1 = stack.pop()
                i2 = stack.pop()
                if t == '+':
                    stack.append(i1+i2)
                elif t == '-':
                    stack.append(i2-i1)
                elif t == '*':
                    stack.append(i1*i2)
                elif t == '/':
                    stack.append(int(i2/i1))
            else:
                stack.append(int(t))

        return stack.pop()

print(Solution().evalRPN(tokens = ["4","13","5","/","+"]))