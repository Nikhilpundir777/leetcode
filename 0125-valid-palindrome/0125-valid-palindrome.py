class Solution(object):
    def isPalindrome(self, s):
        cleaned_str = ''.join([char.lower() for char in s if char.isalnum()])
        if cleaned_str==cleaned_str[::-1]:
            return True
        else:
            return False
        