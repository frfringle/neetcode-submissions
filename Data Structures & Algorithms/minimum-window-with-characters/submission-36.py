from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        if s == t: return s

        need = Counter(t)
        have = Counter({})
        
        need_n = len(need)
        have_n = 0

        longest_sub = s + "a"

        left = 0
        for r in range(len(s)):
            char = s[r]
            have[char] += 1
            if have[char] == need[char]:
                have_n += 1
                while have_n == need_n:
                    if have[s[left]] == need[s[left]]:
                        
                        have_n -= 1
                        longest_sub = min(longest_sub, s[left:r + 1], key=len)
                    have[s[left]] -= 1
                    left += 1
        if longest_sub == s + "a":
            return ""
        return(longest_sub)
