class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # Initialize the output array with 1s

        left = 1
        for i in range(n):
            output[i] *= left  # Multiply the current value by the product of elements to the left
            left *= nums[i]    # Update left to include nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right  # Multiply the current value by the product of elements to the right
            right *= nums[i]    # Update right to include nums[i]

        return output