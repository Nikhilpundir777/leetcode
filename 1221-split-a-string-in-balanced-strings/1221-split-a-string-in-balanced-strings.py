class Solution(object):
    def balancedStringSplit(self, s):
        count = 0  # To count the number of balanced strings
        r = 0  

        for char in s:
            if char == 'R':
                r += 1 
            elif char == 'L':
                r -= 1 

            if r == 0:  # A balanced string is found when r becomes 0
                count += 1

        return count