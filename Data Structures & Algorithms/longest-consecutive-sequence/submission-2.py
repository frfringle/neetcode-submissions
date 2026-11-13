class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1: return 0
        sort = sorted(set(nums))
        longest = 1
        currentseq = 1
        print(sort)
        for i in range(1, len(sort)):
            if sort[i] == sort[i-1] + 1:
                currentseq += 1
                longest = max(longest, currentseq)
            else:
                currentseq = 1
        return longest
