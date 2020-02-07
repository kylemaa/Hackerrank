# https://www.hackerrank.com/challenges/capitalize/problem
import os


def solve(s):
    # x is the first character of s
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
