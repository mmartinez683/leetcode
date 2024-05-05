class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        max_wealth = 0 
        for money in accounts:
            wealth_sum = sum(money)
            max_wealth = max(max_wealth, wealth_sum)

        return max_wealth
