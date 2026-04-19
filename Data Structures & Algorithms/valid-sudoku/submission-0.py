class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = {}
        colMap = {}
        boxMap = {}

        for i in range(9):
            rowMap[i] = set()
            colMap[i] = set()
            boxMap[i] = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                # check row
                if val in rowMap[i]:
                    return False
                rowMap[i].add(val)

                # check col
                if val in colMap[j]:
                    return False
                colMap[j].add(val)

                # check box
                box = (i // 3) * 3 + (j // 3)
                if val in boxMap[box]:
                    return False
                boxMap[box].add(val)

        return True