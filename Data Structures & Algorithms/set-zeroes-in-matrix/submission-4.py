class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r, c = len(matrix), len(matrix[0])
        rowZero = False

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[0][j] = False
                    if i > 0:
                        matrix[i][0] = False
                    else:
                        rowZero = True

        # print(matrix)

        for i in range(1, r):
            for j in range(1, c):
                if matrix[0][j] == False or matrix[i][0] == False:
                    matrix[i][j] = 0
        
        # print(matrix)

        for i in range(1, r):
            if matrix[i][0] == False:
                matrix[i][0] = 0
        
        for j in range(1, c):
            if matrix[0][j] == False:
                matrix[0][j] = 0

        if matrix[0][0] == False:
            for a in range(r):
                matrix[a][0] = 0
        
        if rowZero:
            for b in range(c):
                matrix[0][b] = 0

        # print(matrix)

