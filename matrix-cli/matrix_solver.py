from .matrix import Matrix

class MatrixSolver:

    def to_ref(self, matrix):

        # Attempts to remove 0 at pivot points
        for diag in range(matrix.rows):
            if matrix[diag][diag] == 0:
                for row in range(diag, matrix.rows):
                    if matrix[row][diag] != 0:
                        matrix.swap_rows(diag, row)

        for col in range(matrix.rows):
            if(matrix[col][col] != 1 and matrix[col][col] != 0):
                matrix.multiply_row(col, 1 / matrix[col][col])
            for row in range(col + 1, matrix.rows):
                if not matrix[row][col] == 0:
                    matrix.add_row(row, col, matrix[row][col] / matrix[col][col] * -1)

        return matrix

    def to_rref(self, matrix):
        self.to_ref(matrix)
        for col in range(matrix.rows - 1, -1, -1):
            for row in range(col - 1, -1, -1):
                if not matrix[col][col] == 0:
                    matrix.add_row(row, col, matrix[row][col] / matrix[col][col] * -1)

        return matrix
