from collections import Counter
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq=Counter(nums)
         
        # Extract all numbers (sorted in descending order)
        sorted_nums = sorted(freq.elements(), reverse=True)
        
        # Return the k-th largest number (1-indexed)
        return sorted_nums[k-1]