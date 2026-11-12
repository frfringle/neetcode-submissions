from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            counterized = tuple(sorted(string))
            ans[counterized].append(string)
        return list(ans.values())
        
        