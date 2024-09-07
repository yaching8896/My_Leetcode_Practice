class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count = {}
        # for i in nums:
        #     if i in count:
        #         count[i] += 1
        #     else:
        #         count[i] = 1
        # return list(count.keys())[list(count.values()).index(1)]
        uniq = 0
        for i in nums:
            uniq ^= i
        return uniq