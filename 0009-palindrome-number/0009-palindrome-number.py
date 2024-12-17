class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrome = str(x)
        return palindrome == palindrome[::-1]