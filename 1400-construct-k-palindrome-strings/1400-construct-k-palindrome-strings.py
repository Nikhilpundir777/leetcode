class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Step 1: Check basic constraints
        if k > len(s):  # More palindromes than characters
            return False
        if k < 0:  # k cannot be negative
            return False

        # Step 2: Count character frequencies
        freq = Counter(s)

        # Step 3: Count the number of odd frequencies
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)

        # Step 4: Check if it's possible to construct k palindromes
        return odd_count <= k