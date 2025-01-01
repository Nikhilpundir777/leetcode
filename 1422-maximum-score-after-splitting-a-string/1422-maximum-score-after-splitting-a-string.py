class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        
        # Loop through all possible split points
        for i in range(1, len(s)):  # Exclude splitting at the first or last character
            left = s[:i]            # Left substring
            right = s[i:]           # Right substring
            
            # Calculate the score: number of '0's in left + number of '1's in right
            score = left.count('0') + right.count('1')
            
            # Update max_score if the current score is higher
            max_score = max(max_score, score)
        
        return max_score
        