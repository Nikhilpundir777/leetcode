class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  # Initialize pointers
        max_area = 0
        
        while left < right:
            # Calculate the area with the current left and right pointers
            width = right - left
            height_of_container = min(height[left], height[right])
            current_area = width * height_of_container
            
            # Update the maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area