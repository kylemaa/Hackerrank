# https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName, lastName, idNumber)
        self.scores = scores
    
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    
    #   Function Name: calculate
    def calculate(self):
        res_char = ''
        average = sum(self.scores)/len(self.scores)
        if average >= 90 and average <= 100:
            res_char = 'O'
        elif average >= 80 and average < 90: 
            res_char = 'E'
        elif average >= 70 and average < 80:
            res_char = 'A'
        elif average >= 55 and average < 70:
            res_char = 'P'
        elif average >= 40 and average < 55:
            res_char = 'D'
        else:
            res_char = 'T'
        return res_char


    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())