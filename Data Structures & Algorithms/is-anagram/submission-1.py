class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter

        # s_count = Counter(s)
        # t_count = Counter(t)

        # return s_count == t_count

        if len(s) != len(t):
            return False

        count = [0] * 26

        i = 0
        while i < len(s):
            x = ord(s[i]) - ord('a')
            y = ord(t[i]) - ord('a')

            count[x] += 1
            count[y] -= 1

            i += 1

        if count != [0] * 26:
            return False
        
        return True