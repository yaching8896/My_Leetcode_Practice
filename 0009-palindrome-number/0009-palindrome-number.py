class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i in range(len(str(x))):
            if str(x)[i] != str(x)[-i-1]:
                return False
        return True
