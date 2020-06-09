class Matrix():

    def __init__(self, contents):
        self.contents = contents

    def __str__(self):
        output = ''
        for row in self.contents:
            output += str(row) + '\n'
        return output

    def swap_rows(self, row1, row2):
        placeHolder = self.contents(row1)
        self.contents[row1] = self.contents[row2]
        self.contents[row2] = placeHolder
