# Function for the Nth Fib number using dp memoiz method. Time complexity is O(2^n)


def fibmemoiz(n):
    memo = []
    if memo[n] != null:
        return memo[n]
    if n == 1 or n == 2:
        result = 1 
    else:
        result = fibmemoiz(n-1) + fibmemoiz(n-2)
        memo[n] = result 

