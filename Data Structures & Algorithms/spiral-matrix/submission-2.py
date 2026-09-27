class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row, start_col = 0, 0
        start_hor, start_ver = len(matrix[0]) - 1, len(matrix) - 1

        res = []

        while start_hor > 0 and start_ver > 0:
            i, j = start_row, start_col
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
            
        if start_ver == 0 and start_hor >= 0:      # single row left
            for a in range(start_hor + 1):
                res.append(matrix[start_row][start_col + a])
        elif start_hor == 0 and start_ver > 0:     # single column left
            for b in range(start_ver + 1):
                res.append(matrix[start_row + b][start_col])
        

        return res

            


