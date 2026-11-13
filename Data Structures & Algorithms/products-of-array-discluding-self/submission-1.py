class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        total = 1
        zero_index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index.append(i)
            else:
                total *= nums[i]
        if len(zero_index) >= 2:
            return [0] * len(nums)
        elif len(zero_index) == 1:
            ret = [0] * len(nums)
            ret[zero_index[0]] = total
            return ret

        for i in nums:
            if i == 0:
                ret.append(total)
            else:
                ret.append(int(total/i))
        return ret
