class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        l = 0

        nodups = set()

        for i in range(len(s)):
            while s[i] in nodups:
                nodups.remove(s[l])
                l += 1
            
            nodups.add(s[i])

            longest = max(longest, i - l + 1)
        
        return longest