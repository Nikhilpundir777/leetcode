class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.all_substring(s)  # Return the result from all_substring

    def all_substring(self, s: str) -> str:
        longest_palindrome = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):  # Include the last index
                substring = s[i:j]

                # Check if the substring is a palindrome and update the longest one
                if self.is_palindrome(substring) and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
        return longest_palindrome  # Return the longest palindrome found

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]  # Check if the string is the same as its reverse


        