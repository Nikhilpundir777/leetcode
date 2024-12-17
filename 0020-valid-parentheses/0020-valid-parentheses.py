class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack
        mapping = {')': '(', '}': '{', ']': '['}  # Create a mapping for closing -> opening brackets
        
        for char in s:  # Iterate through each character in the string
            if char in mapping:  # Check if the character is a closing bracket
                # Pop the top of the stack if not empty; otherwise, assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Compare the popped element with the corresponding opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were properly closed
        return not stack