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

    def swap_rows(self, row1, row2):
        placeHolder = self.contents[row1]
        self.contents[row1] = self.contents[row2]
        self.contents[row2] = placeHolder

    def add_row(self, row1, row2, multiplier):
        for col in range(len(self[0])):
            self.contents[row1][col] += self[row2][col] * multiplier 

    def multiply_row(self, row, multiplier):
        for col in range(len(self[row])):
            self.contents[row][col] = self[row][col] * multiplier

    def __getitem__(self, row):
        return self.contents[row]
