# https://leetcode.com/problems/valid-parentheses/


def validParantheses(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append('(')
        if c == ')':
            if len(stack) == 0:
                return False
            if stack[-1] != '(':
                return False
            else:
                stack.pop()

        if c == '[':
            stack.append('[')
        if c == ']':
            if len(stack) == 0:
                return False
            if stack[-1] != '[':
                return False
            else:
                stack.pop()

        if c == '{':
            stack.append('{')
        if c == '}':
            if len(stack) == 0:
                return False
            if stack[-1] != '{':
                return False
            else:
                stack.pop()

        # egde case
    if len(stack) > 0:
        return False
    else:
        return True


s = '()[]'
print(validParantheses(s))
