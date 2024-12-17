class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows_to_zero = set()
        cols_to_zero = set()

    # Step 1: Identify rows and columns to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        # Step 2: Set rows and columns to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows_to_zero or j in cols_to_zero:
                    matrix[i][j] = 0
            