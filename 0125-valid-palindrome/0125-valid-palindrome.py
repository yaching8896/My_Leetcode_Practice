class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()] 
        print(s)
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        
        return True