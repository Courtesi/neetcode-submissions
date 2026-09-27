class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no_dups = set(nums)
        max_seq = 0
        
        for i in nums:
            if i - 1 not in no_dups:
                count = 1
                start = i
                while start + 1 in no_dups:
                    count += 1
                    start += 1
                
                max_seq = max(max_seq, count)
            
        
        return max_seq