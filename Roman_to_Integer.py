class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        prev_value = 0

        for i in range(len(s)):
            current_value = roman_val[i]
            total += current_value

            if prev_value < current_value:
                total -= 2 * prev_value  
            prev_value = current_value

        return total
