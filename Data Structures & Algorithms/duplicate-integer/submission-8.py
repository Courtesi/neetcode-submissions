class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) == 0:
        #     return False

        # from collections import Counter

        # count = Counter(nums)

        # print(count.values())

        # x = set(count.values())

        # if x == {1}:
        #     return False

        # return True

        count = set()
        for i in nums:
            if i in count:
                return True
            count.add(i)
        
        return False