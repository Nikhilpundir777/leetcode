class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Function to split digits of a number and return as a string
        def digit_repr(num):
            if num < 10:
                return str(num)
            else:
                # Return the string representation of the number itself
                return str(num)
        
        # Sort nums based on custom sorting logic
        nums_str = list(map(str, nums))
        
        # Custom sorting: Compare concatenations
        nums_str.sort(key=lambda x: x * 10, reverse=True)  # Multiply to compare "repeatability"

        # Join the numbers into the largest number string
        result = ''.join(nums_str)
        
        # Handle the edge case of all zeros
        return '0' if result[0] == '0' else result