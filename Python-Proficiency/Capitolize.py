def solve(s):
    s = input()
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    print(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
