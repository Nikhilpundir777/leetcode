class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:  # Handle empty input
            return 0

        longest = 1  # At least a single element counts
        inc, dec = 1, 1  # Initialize counters for increasing and decreasing subarrays

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Increasing subarray
                inc += 1
                dec = 1  # Reset decreasing count
            elif nums[i] < nums[i - 1]:  # Decreasing subarray
                dec += 1
                inc = 1  # Reset increasing count
            else:  # No change
                inc = dec = 1

            # Update the longest subarray length
            longest = max(longest, inc, dec)

        return longest