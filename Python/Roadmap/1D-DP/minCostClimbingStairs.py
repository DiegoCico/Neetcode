class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2: 
            return cost[-1]
        
        for i in range(2, len(cost)):
            left = cost[i-2] + cost[i]
            right = cost[i-1] + cost[i]
            cost[i] = min(left, right)
        print(cost)
        return min(cost[-1], cost[-2])
        