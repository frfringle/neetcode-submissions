class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        current_max = min(heights[left], heights[right]) * (right - left)
        while left < right:
            left_v = heights[left]
            right_v = heights[right]

            current_max = max(current_max, min(heights[left], heights[right]) * (right - left))      
            

            if left_v > right_v:
                right -= 1
            else:
                left += 1
        return current_max