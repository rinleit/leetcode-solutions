class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        diff = 10**7
        for i in range(0, n-1): 
            # initialize left and right 
            l = i + 1
            r = n - 1
            x = nums[i] 
            while (l < r):
                sum3 = x + nums[l] + nums[r]
                if (sum3 == target):
                    return sum3
                elif (sum3 < target): 
                    l+=1
                else: 
                    r-=1
                dff = abs(sum3 - target)
                if dff < diff:
                    diff = dff
                    ans = sum3
        return ans
        