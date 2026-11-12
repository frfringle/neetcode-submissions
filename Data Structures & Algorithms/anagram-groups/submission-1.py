from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs:
            counterized = tuple(sorted((string)))
            
            if counterized in ans:
                ans[counterized].append(string)
            else:
                ans[counterized] = [string]
        return list(ans.values())
        
        