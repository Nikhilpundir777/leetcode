class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for word in strs:
            # Sort the characters in the word to create a "key" for the group
            key = "".join(sorted(word))
            
            # Add the word to the appropriate group in the dictionary
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        
        # Return all grouped anagrams as a list of lists
        return list(anagrams.values())
        
        