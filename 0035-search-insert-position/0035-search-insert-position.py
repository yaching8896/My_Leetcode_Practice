class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        site = 0
        for i in nums:
            if i < target:
                site +=1

        return site