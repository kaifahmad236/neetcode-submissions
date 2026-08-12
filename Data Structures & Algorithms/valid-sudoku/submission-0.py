class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row= [set() for _ in range(9)]
        col= [set() for _ in range(9)]
        box= [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                b= (r//3)*3 +(c//3)

                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False
                if board[r][c] in box[b]:
                    return False

                row[r].add(board[r][c])
                col[c].add(board[r][c])
                box[b].add(board[r][c])
        return True