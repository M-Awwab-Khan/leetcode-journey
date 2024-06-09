class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idk wth is it not working on leetcode
        # l, r = 0, len(matrix) - 1

        # # finding the best possible row
        # while l < r:
        #     mid = (l + r) // 2
        #     if target < matrix[mid][0]:
        #         r = mid - 1
        #     else:
        #         l = mid

        # left, right = 0, len(matrix[l]) - 1

        # #finding the element in that row
        # while left < right:
        #     mid = (left + right) // 2
        #     if target < matrix[l][mid]:
        #         right = mid - 1
        #     else:
        #         left = mid

        # if matrix[l][left] == target:
        #     return True
        # return False

        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row, mid_col = divmod(mid, n)  # dividing mid by no of cols will give which row, mid lies in
                                               # moduling mid by no of cols will give which col, mid lies in

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False