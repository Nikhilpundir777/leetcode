class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_a = set()
        seen_b = set()
        prefix_common = []
        common_count = 0
        
        for i in range(len(A)):
            if A[i] in seen_b:
                common_count += 1
            if B[i] in seen_a:
                common_count += 1
            if A[i] == B[i]:
                common_count += 1  # Account for matching elements at the same index
            
            seen_a.add(A[i])
            seen_b.add(B[i])
            
            prefix_common.append(common_count)
        
        return prefix_common