# https://leetcode.com/problems/valid-parentheses/


def validParantheses(s):
    """This function returns True if a string contain valid parentheses else returns False"""
    # Check if the length of the string is even
    if len(s) % 2 != 0:
        return False
    # Declare a stack to match close/open brackets
    stack = []
    # Dictionary with open brackets as key
    par = {'(': ')', '[': ']', '{': '}'}
    # Iterate the given string and append the open brackets
    for character in s:
        if character in par.keys():
            stack.append(character)
        # Pop the open bracket if there is a matching close bracket
        if len(stack) != 0 and character == par[stack[-1]]:
            stack.pop()
    # Check again to see if all the open brackets are popped
    if len(stack) == 0:
        return True
    return False


s = '[]](){}'
print(validParantheses(s))  # Should return False
