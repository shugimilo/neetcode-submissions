class Solution:
    def convertToCoords(self, position: int, n: int) -> tuple(int, int):
        row = position // n
        col = position % n

        return (row, col)

    def convertToPosition(self, m: int, n: int, row: int, col: int) -> int:
        return row * n + col

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        zeros = []

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    zeros.append(self.convertToPosition(m, n, i, j))

        for zero in zeros:
            row, col = self.convertToCoords(zero, n)
            matrix[row] = [0] * n
            for i in range(0, m):
                matrix[i][col] = 0
            

        