class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for row in matrix:
        #     if row[0] <= target and row[-1] >= target:
        #         l, r = 0, len(row) - 1
        #         while l <= r:
        #             mid = (l + r) // 2
        #             if target == row[mid]:
        #                 return True
        #             elif target < row[mid]:
        #                 r = mid - 1
        #             else: 
        #                 l = mid + 1
        #         if row[l] == target:
        #             return True
        # return False
        
        m = len(matrix)
        n = len(matrix[0])

        if m == 0 or n == 0:
            return False

        row = m-1
        col = 0

        # move up if element > target to make element smaller
        # if element is smaller than the target we got to move in this row across columns
        while col < n and row >= 0:
            element = matrix[row][col]
            if element > target:
                row -= 1
            elif element < target:
                col += 1
            else:
                return True
        return False