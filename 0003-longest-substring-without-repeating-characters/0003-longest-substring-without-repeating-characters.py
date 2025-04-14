class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
            
        string = ""
        length = 0
        for i in s:
            if i in string:
                length = max(len(string), length)  
                string = f"{i}"
            else:
                string += i
        return length
