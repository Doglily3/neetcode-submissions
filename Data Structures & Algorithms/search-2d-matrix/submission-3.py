class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while up <= down:
            mid_row = (down + up) // 2
            if matrix[mid_row][0] > target:
                down = mid_row - 1
            elif matrix[mid_row][right] < target:
                up = mid_row + 1
            else:
                while left <= right:
                    midCol = (left + right) // 2
                    if matrix[mid_row][midCol] < target:
                        left = midCol + 1
                    elif matrix[mid_row][midCol] > target:
                        right = midCol - 1
                    else:
                        return True
                return False
        return False
