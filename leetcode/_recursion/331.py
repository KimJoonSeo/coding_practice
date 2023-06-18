class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        preorder = preorder.split(',')
        for value in preorder:
            if value == '#':
                if len(stack) >=2 and stack[-1] == '#' and stack[-2] != '#':
                    stack.pop()
                    stack.pop()
                    stack.append('#')
                    self.recursion(stack)
                else:
                    stack.append(value)
            else:
                stack.append(value)

        return stack == ['#']

    def recursion(self, stack):
        if len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
            stack.pop()
            stack.pop()
            stack[-1] = '#'
            self.recursion(stack)


print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))