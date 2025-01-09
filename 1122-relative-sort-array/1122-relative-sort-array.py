class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # a dictionary to store the order of elements in arr2
        order = {num: index for index, num in enumerate(arr2)}
        
        # Use sorted with a custom key function
        return sorted(arr1, key=lambda x: (order.get(x, len(arr2)), x))