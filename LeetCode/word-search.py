class Grid(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def wordSearch(self, word):
        for i in range(len(matrix)):
            if self.wordSearchRight(i, word):
                return True 
        for i in range(len(matrix)):
            if self.wordSearchDown(i, word):
                return True
        return False
            

    def wordSearchRight(self,index, word):
        for i in range(len(self.matrix[index])):
            if word[i] != matrix[i][index]:
                return False 
        return True

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

print(Grid(matrix).wordSearch('FACI'))