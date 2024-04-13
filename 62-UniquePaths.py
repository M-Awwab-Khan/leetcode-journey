class Solution:
    # def uniquePaths(self, m: int, n: int, memo: dict = {}) -> int:
    #     if (f'{m},{n}' in memo) or (f'{n},{m}' in memo):
    #         return memo[f'{m},{n}']
    #     if m == 0 or n == 0:
    #         return 0
    #     if m == 1 or n == 1:
    #         return 1
        
    #     memo[f'{m},{n}'] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)
    #     memo[f'{n},{m}'] = memo[f'{m},{n}']
    #     return memo[f'{m},{n}']
    def uniquePaths(self, m, n):
        @cache
        def dfs(i, j):
            if i >= m or j >= n:      return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)
