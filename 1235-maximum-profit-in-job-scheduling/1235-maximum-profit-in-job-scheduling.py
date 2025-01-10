class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
         # Combine the jobs and sort by endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [(0, 0)]  # (endTime, maxProfit)

        for start, end, prof in jobs:
            # Use binary search to find the last job that ends before or at the start of the current job
            i = bisect_right(dp, (start, float('inf'))) - 1
            # Calculate the current profit by including this job
            current_profit = dp[i][1] + prof
            # Only add to DP if it increases the total profit
            if current_profit > dp[-1][1]:
                dp.append((end, current_profit))
        
        return dp[-1][1]