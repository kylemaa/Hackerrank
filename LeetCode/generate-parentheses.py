def generateParentheses(n):
    """This function call backtrack() to create valid parentheses"""
    res = []

    def backtrack(S, left, right):
        if len(S) == n*2:
            res.append(S)
            return
        # left variable would increment from 0
        if left < n:
            backtrack(S + '(', left+1, right)
        #  backtracking each incremental with closing brackets
        if left > right:
            backtrack(S + ')', left, right+1)
    # Calling base case
    backtrack("", 0, 0)
    return res


print(generateParentheses(3))
