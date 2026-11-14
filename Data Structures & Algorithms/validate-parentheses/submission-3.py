class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        stk = []
        closers = {")":"(", "}":"{","]":"["}
        for i in s:
            if i in closers:
                if stk and stk[-1] == closers[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        return not stk