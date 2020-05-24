class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left, right, n = nums[0], nums[-1], len(nums)
        max_prod = max(left, right)
        for i in range(1, n):
            left = left*nums[i] or nums[i]
            right = right*nums[n-i-1] or nums[n-i-1]
            max_prod = max(left, right, max_prod)
        return max_prod
