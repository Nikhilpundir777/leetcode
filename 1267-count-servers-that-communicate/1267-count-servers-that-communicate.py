class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Step 1: Calculate the number of servers in each row and column
        rows = [sum(row) for row in grid]
        cols = [sum(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        
        # Step 2: Count servers that can communicate
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If there's a server and it can communicate via row or column
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1
                    
        return count
