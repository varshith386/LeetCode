class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        var = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in var.values():
                stk.append(char)
            elif char in var.keys():
                if not stk or stk.pop() != var[char]:
                    return False
            else:
                return False

        return not stk
