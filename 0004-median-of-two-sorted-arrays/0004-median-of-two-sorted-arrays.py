import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        sorted_nums=sorted(nums)
        return statistics.median(sorted_nums)
        
        