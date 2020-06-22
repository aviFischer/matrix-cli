class Matrix():

    def __init__(self, contents):
        self.contents = contents
        self.rows = len(contents)
        self.cols = len(contents[0])

    def __str__(self):
        output = ''
        for row in self.contents:
            output += str(row) + '\n'
        output = output[0:len(output) - 1]
        return output

    def __getitem__(self, row):
        return self.contents[row]

    def swap_rows(self, row1, row2):
        """ 
        Swaps two rows of the matrix

        Parameters:

            row1: The first row to be swapped

            row2: The second row to be swapped
        """
        placeHolder = self.contents[row1]
        self.contents[row1] = self.contents[row2]
        self.contents[row2] = placeHolder

    def add_row(self, row1, row2, multiplier):
        """ 
        For each collumn in the matrix, adds the element of row2 in
        the collum multiplied by multiplier to the element in row1

        Parameters:

            row1: The row to be added to

            row2: The row that will be added to row 1

            multiplier: The factor to multiply each element of row2 by before it is added to row1
        """
        for col in range(len(self[0])):
            self.contents[row1][col] += self[row2][col] * multiplier 

    def multiply_row(self, row, multiplier):
        """ 
        Multiplies every item in the specifyed row by multiplier

        Parameters:

            row: The row to be multiplyed

            multiplier: The factor to multiply each element of row by
        """
        for col in range(len(self[row])):
            self.contents[row][col] = self[row][col] * multiplier

    def sub_matrix(self, row, col):
        """ 
        Creates a new matrix with the specified row 
        and collumn removed from the current matrix

        Parameters:

            row: The row to be removed

            col: The collumn to be removed

        Returns:

            A new, smaller matrix
        """

        newContents = []

        for i in range(row):
            newContents.append([])
            for j in range(col):
                newContents[i].append(self[i][j])
            for j in range(col + 1, self.cols):
                newContents[i].append(self[i][j])
        for i in range(row + 1, self.rows):
            newContents.append([])
            for j in range(col):
                newContents[i].append(self[i][j])
            for j in range(col + 1, self.cols):
                newContents[i - 1].append(self[i][j])

        return Matrix(newContents)
