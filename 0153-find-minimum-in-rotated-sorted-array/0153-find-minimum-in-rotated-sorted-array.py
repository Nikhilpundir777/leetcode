class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Assume the first element is the minimum
        min_val = nums[0]
        
        # Traverse through the array to find the minimum element
        for num in nums:
            if num < min_val:
                min_val = num
        
        return min_val