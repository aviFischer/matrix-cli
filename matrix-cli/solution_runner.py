from .matrix import Matrix
from .matrix_solver import MatrixSolver

class SolutionRunner:
    def __init__(self, args):
        self.args = args

    def string_to_matrix(self, matrix_str):
        matrix_str = matrix_str.replace(' ', '') #removes any spaces
        matrix_str = matrix_str[2:len(matrix_str) - 3] #trims trailing square brackets
        row_array = matrix_str.split('],[') #splits into rows

        matrix = []

        for row in row_array:
            element_array = row.split(',')
            for index in range(len(element_array)):
                element_array[index] = float(element_array[index])

        return Matrix(matrix)

    def run(self, args):
        command = args.command
        matrix_solver = MatrixSolver()
        solution = None

        if command == 'to_rref':
            solution = matrix_solver.to_rref(self.string_to_matrix(args.input_matrix))

        if len(args.output) == 0:
            print(solution)
        else:
            f = open(args.output, 'w')
            f.write(solution)
