from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) 
        checkagainst=Counter(s1)
        while r <= len(s2):
            print(s2[l:r])
            if Counter(s2[l:r]) == checkagainst:
                return True
            r+=1
            l += 1
        return False
