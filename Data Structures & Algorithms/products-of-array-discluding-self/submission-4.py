class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [1] * len(nums)

        pref_temp = 1
        suff_temp = 1

        for i in range(len(nums)):
            prefix[i] *= pref_temp
            pref_temp *= nums[i]
            
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] *= suff_temp
            suff_temp *= nums[i]
        
        for i in range(len(res)):
            res[i] = int(suffix[i] * prefix[i])

        return res