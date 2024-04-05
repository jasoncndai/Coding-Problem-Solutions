class Solution:
    def removeStars(self, s: str) -> str:
        # Utilize a stack, insert each character and pop when reaching a *
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)