class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top , bot = 0, ROWS - 1
        while(top <= bot):
            rows = (top + bot)//2
            if target > matrix[rows][-1]:
                top = rows + 1
            elif target < matrix[rows][0]:
                bot = rows - 1
            else:
                break
        if top > bot:
            return False
        rows = (top +bot) // 2
        l, r = 0, COLS - 1
        while (l <= r):
            m = (l + r) // 2
            if target > matrix[rows][m]:
                l = m + 1
            elif target < matrix[rows][m]:
                r = m - 1
            else:
                return True
        return False

    
        