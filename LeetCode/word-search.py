class Grid(object):
    def __init__(self, matrix):
        self.matrix = matrix
    
    # main function to iterate through each row and column element
    def wordSearch(self, word):
        for i in range(len(matrix)):
            if self.wordSearchRight(i, word):
                return True 
        for i in range(len(matrix)):
            if self.wordSearchDown(i, word):
                return True
        return False

    # helper function to search for to the right of each row 
    def wordSearchRight(self,index, word):
        for i in range(len(self.matrix[index])):
            if word[i] != matrix[i][index]:
                return False 
        return True
    # helper function to search for word downward of each column
    def wordSearchDown(self,index, word):
        for i in range(len(self.matrix[index])):
            if word[i] != matrix[index][i]:
                return False 
        return True


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]

# printing class object with method 
print(Grid(matrix).wordSearch('FACI'))