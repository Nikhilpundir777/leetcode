class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Retain only elements not equal to val
        nums[:] = [num for num in nums if num != val]
        return len(nums)