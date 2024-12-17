from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        # Create a list of the corresponding letters for each digit in the input
        groups = [phone_map[digit] for digit in digits]
        
        # Generate all combinations using itertools.product and return as a list
        return [''.join(combo) for combo in product(*groups)]