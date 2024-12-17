class Solution:
    def climbStairs(self, n: int) -> int:
        if (n<=3):
            return n
        
        n1, n2 = 2, 3  # Ways to climb 2 and 3 stairs
        for _ in range(4, n + 1):
            n3 = n1 + n2  
            n1=n2  
            n2=n3
        
        return n2  # Return the total ways to climb `n` stairs
        