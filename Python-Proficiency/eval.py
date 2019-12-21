# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        cmmd = s[0]
        args = s[1:]
        if cmmd != "print":
            cmmd += "(" + ",".join(args) + ")"
            eval("l."+cmmd)
        else:
            print(l)
