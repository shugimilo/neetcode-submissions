class Solution:
    def convertToCoords(self, position: int, n: int) -> tuple(int, int):
        row = position // n
        col = position % n

        return (row, col)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n-1

        while left <= right:
            mid = (left + right) // 2
            midRow, midCol = self.convertToCoords(mid, n)
            if matrix[midRow][midCol] < target:
                left = mid + 1
            elif matrix[midRow][midCol] > target:
                right = mid - 1
            else:
                return True

        return False

