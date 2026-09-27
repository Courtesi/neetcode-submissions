class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        quadrant_dup = defaultdict(set)
        row_dup = defaultdict(set)
        col_dup = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                quadrant_i = i // 3
                quadrant_j = j // 3

                quadrant = (quadrant_i, quadrant_j)

                if board[i][j] == ".":
                    continue

                # Checking Quadrant
                if quadrant in quadrant_dup and board[i][j] in quadrant_dup[quadrant]:
                    print("quadrant")
                    return False
                
                quadrant_dup[quadrant].add(board[i][j])

                # Checking Rows
                if i in row_dup and board[i][j] in row_dup[i]:
                    print("row", i, j, board[i][j])
                    return False
                
                row_dup[i].add(board[i][j])

                # Checking Cols
                if j in col_dup and board[i][j] in col_dup[j]:
                    print("col")
                    return False
                
                col_dup[j].add(board[i][j])
        
        return True
