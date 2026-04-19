class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        for i in range(9):
            row[i] = set()
            col[i] = set()
            box[i] = set()
        
        for i in range(9):
            for j in range(9):
                
                val = board[i][j]
                if val == ".":
                    continue

                if val in row[i]:
                    return False
                row[i].add(val)

                if val in col[j]:
                    return False
                col[j].add(val)

                boxn = i // 3 * 3 + j // 3
                if val in box[boxn]:
                    return False
                box[boxn].add(val)
        return True