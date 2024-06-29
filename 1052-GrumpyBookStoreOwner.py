class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_diff = 0
        powerup_position = -1
        for i in range(len(customers) - minutes + 1):
            if i == 0:
                before_powerup = sum(c*(1 - g) for (c, g) in zip(customers[:minutes], grumpy[:minutes]))
                after_powerup = sum(customers[:minutes])
            else:
                before_powerup -= customers[i - 1] * (1- grumpy[i - 1])
                before_powerup += customers[i + minutes - 1] * (1 - grumpy[i + minutes - 1])

                after_powerup -= customers[i - 1]
                after_powerup += customers[i + minutes - 1]

            if after_powerup - before_powerup > max_diff:
                max_diff = max(max_diff, after_powerup - before_powerup)
                powerup_position = i

        grumpy[powerup_position: powerup_position+minutes] = [0] * minutes
        return sum(c*(1- g) for (c, g) in zip(customers, grumpy))