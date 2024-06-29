class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def possible(force: int) -> bool:
            ball_position = 0
            max_balls = 1
            for pos in range(len(position)):
                if (position[pos] - position[ball_position]) >= force:
                    max_balls += 1
                    ball_position = pos

            return max_balls >= m


        l, r = 1, position[-1] - position[0]
        while l <= r:
            mid: int = (l + r) // 2

            if possible(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r