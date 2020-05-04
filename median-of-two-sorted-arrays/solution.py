class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2); nums1.sort()
        n = len(nums1)
        k = n//2
        if n % 2 == 0:
            return sum(nums1[k-1:k+1])/2
        else:
            return nums1[k]
