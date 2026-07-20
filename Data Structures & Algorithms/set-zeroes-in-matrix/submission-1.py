class Solution:
    def convertToCoords(self, position: int, n: int) -> tuple(int, int):
        row = position // n
        col = position % n

        return (row, col)

    def convertToPosition(self, row: int, col: int) -> int:
        return row * m + col * n

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        zeros = []

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    zeros.append([i, j])

        for zero in zeros:
            row = zero[0]
            col = zero[1]
            print(f'row: {row}, col: {col}')
            matrix[row] = [0] * n
            for i in range(0, m):
                matrix[i][col] = 0
            

        