from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for c in string:
                arr[ord(c) - ord("a")] += 1
            ans[tuple(arr)].append(string)
        return list(ans.values())
        
        