class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_list = [0] * len(height)
        suffix_list = [0] * len(height)

        prefix = height[0]
        suffix = height[-1]

        for i in range(len(height)):
            if height[i] > prefix:
                prefix = height[i]
            
            prefix_list[i] = prefix
        
        for i in range(len(height) - 1, -1, -1):
            if height[i] > suffix:
                suffix = height[i]
            
            suffix_list[i] = suffix
        
        res = 0

        for i in range(len(height)):
            res += min(prefix_list[i], suffix_list[i]) - height[i]
        
        return res
        