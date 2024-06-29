class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        submat: dict[tuple, list] = {}
        for row in range(9):
            for col in range(9):
                submat_dimension = (row // 3, col // 3)
                # checking 3x3 grid
                element = board[row][col]
                if element == ".": continue
                if submat_dimension not in submat:
                    submat[submat_dimension] = [element]
                else:
                    if element in submat[submat_dimension]:
                        return False
                    else:
                        submat[submat_dimension].append(element)

                # traversing that row
                for t_col in range(9):
                    if t_col == col: continue
                    if board[row][t_col] == element:
                        return False
                
                # traversing that column
                for t_row in range(9):
                    if t_row == row: continue
                    if board[t_row][col] == element:
                        return False
                
        return True