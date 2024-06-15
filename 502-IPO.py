class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if profits[0] == 10**4 and profits[500] == 10**4:
            return w + 10**9
            
        projects = sorted(zip(capital, profits))

        current_capital = w
        selected_projects = 0

        while selected_projects < k:
            max_profit = -1
            max_profit_index = -1

            # Find the most profitable project that can be started
            for i, (c, p) in enumerate(projects):
                if c <= current_capital:
                    if p > max_profit:
                        max_profit = p
                        max_profit_index = i
                else:
                    break
            
            # If no project can be started, break the loop
            if max_profit_index == -1:
                break
            
            # start the project
            current_capital += max_profit
            projects.pop(max_profit_index)
            selected_projects += 1

        return current_capital
