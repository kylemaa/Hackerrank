class Solution:
    def uniquePaths(self, m, n):
        matrix = []
        # appending n columns to m rows
        for i in range(m):
            matrix.append([0]*n)
        # assign value 1 to columns and rows
        for i in range(m):
            matrix[i][0] = 1
        for j in range(n):
            matrix[0][j] = 1
        # for each element in the matrix, accumulate the values of the adjacents n-1 and m-1
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        return matrix[m-1][n-1]
