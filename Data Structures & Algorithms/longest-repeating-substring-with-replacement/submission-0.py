class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        most_chars_num = 0

        from collections import defaultdict
        letter_count = defaultdict(int)

        l = 0

        for i in range(len(s)):
            letter_count[s[i]] += 1
            if letter_count[s[i]] > most_chars_num:
                most_chars_num = letter_count[s[i]]

            while i - l + 1 - most_chars_num > k:
                letter_count[s[l]] -= 1
                l += 1

            
            longest = max(longest, i - l + 1)
        
        return longest