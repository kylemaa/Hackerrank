# https://leetcode.com/problems/valid-parentheses/


def validParantheses(s):
    """This function returns True if a string contain valid parentheses else returns False"""

    stack = []
    for character in s:
        # Push the open bracket into the stack
        if character == '(':
            stack.append('(')
        if character == ')':
            # If close bracket starts first then it is not valid
            if len(stack) == 0:
                return False
            # If there is no matching bracket then it is not valid
            if stack[-1] != '(':
                return False
            # If there is a matching bracket then pop the open bracket
            stack.pop()

        # Push the open bracket into the stack
        if character == '{':
            stack.append('{')
        if character == '}':
            # If close bracket starts first then it is not valid
            if len(stack) == 0:
                return False
            # If there is no matching bracket then it is not valid
            if stack[-1] != '{':
                return False
            # If there is a matching bracket then pop the open bracket
            stack.pop()

        # Push the open bracket into the stack
        if character == '[':
            stack.append('[')
        if character == ']':
            # If close bracket starts first then it is not valid
            if len(stack) == 0:
                return False
            # If there is no matching bracket then it is not valid
            if stack[-1] != '[':
                return False
            # If there is a matching bracket then pop the open bracket
            stack.pop()

    # After iterating through the string checks if the stack is empty
    if len(stack) == 0:
        return True
    return False


s = '[]{{}}()'
print(validParantheses(s))
