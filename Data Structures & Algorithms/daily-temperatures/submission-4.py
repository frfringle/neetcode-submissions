class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stk = [(temps[-1], len(temps)-1)]
        for i in range(len(temps) - 2, -1, -1):
            temp = temps[i]
            
            while stk:
                last = stk[-1][0]
                if temp >= last:
                    stk.pop()
                elif temp < last:
                    ans[i] = stk[-1][1] - i
                    break

            stk.append((temp, i))
        return ans
                    
            
                

            
            
