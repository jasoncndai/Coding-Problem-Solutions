class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        d = []
        for p in s:
            if (p == '('):
                d.append('(')
            elif (p == '['):
                d.append('[')
            elif (p == '{'):
                d.append('{')
            elif (p == ')'):
                if len(d) > 0 and '(' == d[-1]:
                    d.pop()
                else:
                    return False
            elif (p == ']'):
                if len(d) > 0 and '[' == d[-1]:
                    d.pop()
                else:
                    return False
            elif (p == '}'):
                if len(d) > 0 and '{' == d[-1]:
                    d.pop()
                else:
                    return False
        
        if len(d) == 0:
            return True
        else:
            return False