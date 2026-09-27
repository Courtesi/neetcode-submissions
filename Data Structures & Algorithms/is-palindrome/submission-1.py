class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while not s[l].isalnum():
                if not (l < r):
                    break
                l += 1
            
            while not s[r].isalnum():
                if not (l < r):
                    break
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True