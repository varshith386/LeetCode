class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_str = str(x)
        
        i, j = 0, len(num_str) - 1
        
        while i < j:
            if num_str[i] != num_str[j]:
                return False
            else:
                i = i+1
                j = j-1
        
        return True
