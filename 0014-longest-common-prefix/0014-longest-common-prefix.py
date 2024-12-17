class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the shortest string in the list
        shortest = min(strs, key=len)
        
        for i in range(len(shortest)):
            for string in strs:
                if string[i] != shortest[i]:
                    return shortest[:i]  # Return prefix up to the mismatch
        
        return shortest  # All strings share the shortest string as a prefix