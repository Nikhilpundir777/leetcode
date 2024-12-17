class Solution(object):
    def rotate(self, matrix):

        self.transpose(matrix)  # Step 1: Transpose the matrix
        self.swap_cols(matrix)  # Step 2: Swap columns to complete the rotation

    def transpose(self, matrix):
        """
        Transpose the matrix in place.
        Swap matrix[i][j] with matrix[j][i] for i < j.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def swap_cols(self, matrix):
        """
        Swap columns to rotate the matrix clockwise.
        Swap matrix[i][j] with matrix[i][n-j-1].
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):  # Swap only half the columns in each row
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]




        