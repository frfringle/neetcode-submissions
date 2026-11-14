class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        peak = height.index(max(height))
        total = 0

        # left side: the tallest bar guarantees a right wall
        left_max = 0
        for i in range(peak):
            left_max = max(left_max, height[i])
            total += left_max - height[i]

        # right side: same thing, scanning backwards
        right_max = 0
        for i in range(len(height) - 1, peak, -1):
            right_max = max(right_max, height[i])
            total += right_max - height[i]

        return total