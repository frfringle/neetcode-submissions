class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l = 0
        r = 1
        longestsub = 1
        while r < len(s):
            if s[r] in s[l:r]:
                l += 1
            else:
                r += 1
                longestsub = max(r-l, longestsub)
        return longestsub