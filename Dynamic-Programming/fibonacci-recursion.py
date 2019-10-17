# Function for the nth Fib number using recursion method. Time complexity is O(n^2)


def fibrecursion(n):
    if n < 0:
        return 'ERROR! Invalid number'
    if n == 1 or n == 0:
        return 1 
    else:
        return fibrecursion(n-1) + fibrecursion(n-2)

