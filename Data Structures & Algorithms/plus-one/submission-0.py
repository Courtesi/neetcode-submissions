class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOver = False

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                carryOver = True
                digits[i] = 0
            else:
                carryOver = False
                digits[i] = digits[i] + 1
                break
            
        if carryOver:
            digits.insert(0, 1)
        
        return digits