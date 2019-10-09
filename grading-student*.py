#https://www.hackerrank.com/challenges/grading/problem

def gradingStudent(grades):
    res = []
    for i in grades:
        if i >= 38 and i % 5 >= 3:
            i += 5-(i%5)
        res.append(i)
    return res
