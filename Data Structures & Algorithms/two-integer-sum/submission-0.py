class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        mapping = defaultdict(list)
        for i, num in enumerate(nums):
            mapping[num].append(i)
        
        for i, num in enumerate(nums):
            if target - num in mapping:
                for mapped in mapping[target - num]:
                    if mapped != i:
                        return [i, mapped]
        
        