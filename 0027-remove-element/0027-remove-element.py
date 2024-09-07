class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        site = 0
        for i in nums:
            if i != val:
                nums[site] = i
                site += 1
                
        
        return site

        