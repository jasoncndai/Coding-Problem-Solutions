class Solution:
    def decodeString(self, s: str) -> str:
        # read string, when reach encoded string put into stack and repeat chars in stack num amount of times
        stack = []
        k = 0
        current_string = ''
        for c in s:
            if c.isdigit():
                # * 10 to account for double/triple/etc. digit numbers
                k = k * 10 + int(c)
            elif c == '[':
                # append previous string and then k to stack
                stack.append((current_string, k))
                k = 0
                current_string = ''
            elif c == ']':
                # pop last string and k for current encoded string, add current string * k
                last_string, last_k = stack.pop()
                current_string = last_string + current_string * last_k
            else:
                current_string += c
        return current_string
                