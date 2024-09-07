class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        
        for i in format(n, 'b'):
            if i == "1":
                total += 1
        return total

