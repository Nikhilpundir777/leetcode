class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0  # To keep track of palindromic substrings

        # Generate all substrings
        for i in range(len(s)):  # Start index
            for j in range(i + 1, len(s) + 1):  # End index (exclusive)
                substring = s[i:j]  # Extract substring
                if substring == substring[::-1]:  # Check if palindrome
                    count += 1  # Increment count if palindrome

        return count  
        