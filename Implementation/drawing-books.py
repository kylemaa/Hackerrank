#https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    half_n = n//2
    right = p//2
    left = half_n - right
    if(right < left):
        return right 
    else:
        return left