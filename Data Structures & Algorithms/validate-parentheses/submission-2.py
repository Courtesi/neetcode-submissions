class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        second = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in second:
                if not stack or (popper := stack.pop()) != second[i]:
                    return False
            else:
                stack.append(i)
        
        return len(stack) == 0