"""This function concates the integer in an array and its duplicate then return the sum"""


def concatenationsSum(a):
    s = ''
    b = []
    for i in a:
        for j in a:
            s += str(i)+str(j)
            b.append(int(s))
            s = ''
    return sum(b)


print(concatenationsSum([10, 2]))  # Expect 1344
