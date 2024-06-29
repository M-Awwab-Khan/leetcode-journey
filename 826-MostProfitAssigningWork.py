class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # BRUTE FORCE (TLE)
        # pft = 0
        # for j in worker:
        #     mx_pft = 0
        #     for i in range(len(difficulty)):
        #         if difficulty[i] <= j:
        #             mx_pft = max(mx_pft, profit[i])
        #     pft += mx_pft


        # return pft

        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        total_profit = 0
        j = 0
        
        for ability in worker:
            while j < len(jobs) and jobs[j][0] <= ability:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            total_profit += max_profit
        
        return total_profit

            
            