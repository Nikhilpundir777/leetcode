class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        
        for i, num in enumerate(nums):
            # Check if the number is already in the dictionary
            if num in last_seen:
                # If the difference between indices is <= k, return True
                if i - last_seen[num] <= k:
                    return True
            # Update the last seen index of the current number
            last_seen[num] = i
        
        # If no such pair is found, return False
        return False
        