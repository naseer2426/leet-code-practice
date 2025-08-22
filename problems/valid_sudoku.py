class Solution:
    def isValidSudoku(self, board):
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        sq = {}
        for i in range(3):
            for j in range(3):
                sq[(i,j)] = {}
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row[i]:
                    # print(f"num already exists in row {i} - {row[i]}")
                    return False
                if num in col[j]:
                    # print(f"num already exists in col {j} - {col[i]}")
                    return False
                if num in sq[(i//3,j//3)]:
                    # print(f"num already exists in sq {(i//3,j//3)} - {sq[(i//3,j//3)]}, num - {num}")
                    return False
                row[i][num] = (i,j)
                col[j][num] = (i,j)
                sq[(i//3,j//3)][num] = (i,j)
                # print(row)
                # print(col)
                # print(sq)
        return True

s = Solution()
print(s.isValidSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))
