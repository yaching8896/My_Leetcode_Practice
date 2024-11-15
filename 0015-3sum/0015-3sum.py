from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 排序數組以便使用雙指針
        ans = []
        length = len(nums)

        for i in range(length - 2):  # 從頭到倒數第三個元素
            if i > 0 and nums[i] == nums[i - 1]:  # 避免重複
                continue
            left, right = i + 1, length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # 跳過重複
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # 跳過重複
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans
