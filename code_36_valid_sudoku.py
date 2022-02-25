class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)
        m = len(board[0])

        grids = [ 
            [board[i][j] for i in range(3) for j in range(3)],
            [board[i][j] for i in range(3,6) for j in range(3)],
            [board[i][j] for i in range(6,9) for j in range(3)],
            [board[i][j] for i in range(3) for j in range(3,6)],
            [board[i][j] for i in range(3,6) for j in range(3,6)],
            [board[i][j] for i in range(6,9) for j in range(3,6)],
            [board[i][j] for i in range(3) for j in range(6,9)],
            [board[i][j] for i in range(3,6) for j in range(6,9)],
            [board[i][j] for i in range(6,9) for j in range(6,9)]
        ]

        # test the rows
        for row in board:
            tester = set()
            for cell in row:
                if cell == '.':
                    continue
                if cell in tester:
                    return False
                tester.add(cell)

        # test the columns
        for col in range(m):
            tester = set()
            for cell in [row[col] for row in board]:
                if cell == '.':
                    continue
                if cell in tester:
                    return False
                tester.add(cell)

        #finally test the grids
        for grid in grids:
            tester = set()
            for cell in grid:
                if cell == '.':
                    continue
                if cell in tester:
                    return False
                tester.add(cell)

        return True