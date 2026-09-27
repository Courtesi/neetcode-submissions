class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_col, start_row = 0, 0
        start_hor, start_ver = len(matrix[0]) - 1, len(matrix) - 1

        res = []

        while start_hor > 0 and start_ver > 0:
            i, j = start_col, start_row
            hor_c, ver_c = start_hor, start_ver

            for top in range(hor_c):
                print(f"{i=}, {j=}")
                res.append(matrix[i][j])
                j += 1
            
            for right in range(ver_c):
                print(f"{i=}, {j=}")
                res.append(matrix[i][j])
                i += 1
            
            for bottom in range(hor_c):
                print(f"{i=}, {j=}")
                res.append(matrix[i][j])
                j -= 1
            
            for left in range(ver_c):
                print(f"{i=}, {j=}")
                res.append(matrix[i][j])
                i -= 1
            
            start_col += 1
            start_row += 1
            start_hor -= 2
            start_ver -= 2
        
        r, c = start_col, start_row  # note: start_col is actually your row index

        if start_ver == 0 and start_hor >= 0:      # single row left
            for a in range(start_hor + 1):
                res.append(matrix[r][c + a])
        elif start_hor == 0 and start_ver > 0:     # single column left
            for b in range(start_ver + 1):
                res.append(matrix[r + b][c])
        
        
        return res

            


