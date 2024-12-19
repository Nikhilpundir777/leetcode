class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_elements=[]
        for i in range(len(nums)):
            if i not in duplicate_elements and nums.count(i)>1:
                duplicate_elements.append(i)
        if duplicate_elements:
            return True
        else:
            return False