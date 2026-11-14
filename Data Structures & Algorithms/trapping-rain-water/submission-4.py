class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height)- 1
        total = 0
        l_h, r_h = 0, 0
        while left< right:
            l_h, r_h = max(height[left], l_h), max(height[right], r_h)
            total += abs(l_h - height[left]) + abs(r_h - height[right])

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return total