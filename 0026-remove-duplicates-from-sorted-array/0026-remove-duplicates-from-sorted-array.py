class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_elements = set()  # Set to track unique elements
        index = 0  # Pointer for the unique position in the list

        for num in nums:
            if num not in unique_elements:
                unique_elements.add(num)
                nums[index] = num  # Update the list in place
                index += 1

        return index  # Return the length of the array with unique elements