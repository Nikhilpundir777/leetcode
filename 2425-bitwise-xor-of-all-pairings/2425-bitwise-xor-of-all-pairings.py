class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        xor1 = 0
        xor2 = 0

        # XOR all elements in nums1
        for num in nums1:
            xor1 ^= num

        # XOR all elements in nums2
        for num in nums2:
            xor2 ^= num

        # Result depends on the parity of the array lengths
        result = 0
        if len(nums2) % 2 == 1:  # If nums2's length is odd, all elements of nums1 contribute
            result ^= xor1
        if len(nums1) % 2 == 1:  # If nums1's length is odd, all elements of nums2 contribute
            result ^= xor2

        return result
