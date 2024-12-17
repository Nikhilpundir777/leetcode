class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:  # Check if complement exists in seen
                return [seen[complement], i]  # Return the indices
            seen[num] = i  # Otherwise, store the current number and its index
        
        return []  
