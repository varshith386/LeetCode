class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freq = {}

        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in t:
            if i in freq:
                freq[i] -= 1
            else:
                return False  

        for count in freq.values():
            if count != 0:
                return False

        return True
