class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = {}
        n = len(nums)
        for i in range(n):
            value = target - nums[i]
            if value not in indexs:
                indexs[nums[i]] = i
            else:
                return [i, indexs[value]]
