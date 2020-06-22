from .matrix import Matrix
from .matrix_solver import MatrixSolver

class InvalidMatrixStringError(Exception):
    def __init__(self, message):
        self.message = f'Couldn\'t parse string \"{message}\" into a matrix'

    def __str__(self):
        return self.message
    

class SolutionRunner:
    def __init__(self, args):
        self.args = args

    def string_to_matrix(self, input):
        matrix_str = input.replace(' ', '') #removes any spaces
        matrix_str = matrix_str[2:len(matrix_str) - 2] #trims trailing square brackets
        row_array = matrix_str.split('],[') #splits into rows

        matrix = []
        try:
            for row in row_array:
                element_array = row.split(',')
                for index in range(len(element_array)):
                    element_array[index] = float(element_array[index])
                matrix.append(element_array)

            return Matrix(matrix)
        except:
            raise(InvalidMatrixStringError(input))

    def run(self):
        command = self.args.command
        matrix_solver = MatrixSolver()
        solution = None

        try:
            if command == 'to-rref':
                solution = matrix_solver.to_rref(self.string_to_matrix(self.args.input_matrix))
            if command == 'determinant':
                solution = matrix_solver.determinant(self.string_to_matrix(self.args.input_matrix))

            if len(self.args.output) == 0:
                print(solution)
            else:
                f = open(self.args.output, 'w')
                f.write(solution)
        except InvalidMatrixStringError:
            print(f'Unable to parse string "{self.args.input_matrix}" into a matrix')
