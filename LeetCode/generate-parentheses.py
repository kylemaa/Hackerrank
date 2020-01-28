def generateParentheses(n):
    res = []

    def backtrack(S, left, right):
        if len(S) == n*2:
            res.append(S)
            return
        if left < n:
            backtrack(S + '(', left+1, right)
        if left > right:
            backtrack(S+')', left, right+1)
    # Calling base case
    backtrack("", 0, 0)
    return res


print(generateParentheses(3))
