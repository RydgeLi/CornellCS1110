class Matrix:
    def __init__(self):
        self.list_of_matrix = []
        self.rows = 0
        self.cols = 0
        
    def build_matrix(self, numbers):  # numbers: list of lists of numbers
        self.rows = len(numbers)
        nc = len(numbers[0])
        bad = False
        for row in numbers:
            if not len(row) == nc:
                bad = True
        if bad:
            return False
        self.list_of_matrix = numbers
        self.cols = nc
    
    def show_matrix(self):
        print('            rows * columns:', self.rows, 'x', self.cols)
        for row in self.list_of_matrix:
            print(row)
        print('\n')
        
    def add(self, other):
        if not (self.rows == other.rows and self.cols == other.cols):
            print("They don't have same size!")
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                self.list_of_matrix[i][j] = self.list_of_matrix[i][j] + other.list_of_matrix[i][j]
        return True
        
    def substract(self, other):
        if not (self.rows == other.rows and self.cols == other.cols):
            print("They don't have same size!")
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                self.list_of_matrix[i][j] = self.list_of_matrix[i][j] - other.list_of_matrix[i][j]
        return True
        
    def multiply(self, other):
        if not self.cols == other.rows:
            print('Failed')
            return False
        result = []
        for i in range(self.rows):
            temp_row = []
            for k in range(other.cols):
                temp = 0
                for j in range(self.cols):
                    temp = temp + self.list_of_matrix[i][j] * other.list_of_matrix[j][k]
                temp_row.append(temp)
            result.append(temp_row)
        return result
    