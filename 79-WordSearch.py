class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        n = len(word)
        def backtrack(i, j, k):
            if k == n:
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = ''
            
            if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
                return True
            
            board[i][j] = temp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False
