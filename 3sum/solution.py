class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        ans = set()
        # sort array elements 
        arr.sort()
        for i in range(0, n-1): 
            # initialize left and right 
            l = i + 1
            r = n - 1
            x = arr[i] 
            while (l < r): 
                if (x + arr[l] + arr[r] == 0): 
                    # print elements if it's sum is zero 
                    ans.add((x, arr[l], arr[r]))
                    l+=1
                    r-=1
                # If sum of three elements is less 
                # than zero then increment in left 
                elif (x + arr[l] + arr[r] < 0): 
                    l+=1
                # if sum is greater than zero than 
                # decrement in right side 
                else: 
                    r-=1
        return list(ans)
        