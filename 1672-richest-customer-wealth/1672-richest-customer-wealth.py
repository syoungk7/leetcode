class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if len(accounts) == 1:
            return sum(accounts[0])
        
        for idx, val in enumerate(accounts):
            if idx == 0:
                max_wealth = sum(accounts[0])
            else:
                if sum(accounts[idx]) > max_wealth:
                    max_wealth = sum(accounts[idx])
        return max_wealth