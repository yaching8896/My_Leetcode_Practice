class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(':')', '{':'}','[':']'}

        for char in s:
            if char in mapping:
                stack.append(char)
            elif len(stack) == 0 or mapping[stack.pop()] != char:
                return False
                
        return len(stack) == 0
        