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

    def determinant(self, matrix):
        if matrix.rows != matrix.cols:
            return 'Couldn\'t take the determinant of a non-square matrix'
        
        if matrix.rows == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix [1][0]

        output = 0
        for i in range(matrix.rows):
            output += matrix[i][0] * self.determinant(matrix.sub_matrix(i, 0))
        
        return output

