class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        
        for i in list("?!,.:; '"):
            s = s.replace(i, "")
            
        right = len(s) - 1
        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True