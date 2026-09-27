class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        l = 0

        nodups = {}

        for i in range(len(s)):
            if s[i] in nodups:
                l = max(nodups[s[i]] + 1, l)            

            nodups[s[i]] = i

            longest = max(longest, i - l + 1)
        
        return longest