class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        lcol = 0
        rcol = len(mat[0])-1
       
        while lcol <= rcol:
            mx_row = 0
            mcol = (rcol+lcol)//2
            
            for row in range(len(mat)):
                mx_row = row if (mat[row][mcol] >= mat[mx_row][mcol]) else mx_row
            
            leftIsBig    =   mcol-1 >= lcol  and  mat[mx_row][mcol-1] > mat[mx_row][mcol]
            rightIsBig   =   mcol+1 <= rcol    and  mat[mx_row][mcol+1] > mat[mx_row][mcol]
            
            if (not leftIsBig) and (not rightIsBig):
                return [mx_row, mcol]

            elif rightIsBig: 
                lcol = mcol+1 
                
            else:  
                rcol = mcol-1
                
        return []