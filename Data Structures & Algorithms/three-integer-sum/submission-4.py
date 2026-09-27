class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(len(nums)):
            target = nums[i]

            if i > 0 and target == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            print(target)

            while l < r:
                if nums[l] + nums[r] > -1 * target:
                    r -= 1
                elif nums[l] + nums[r] < -1 * target:
                    l += 1
                else:
                    res.append([nums[l], nums[r], target])
                    r -= 1
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l - 1]:
                        l += 1
            
            
        
        return res