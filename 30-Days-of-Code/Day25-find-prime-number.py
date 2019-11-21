import math

def prime(value):
    if value == 2:
        return True
    if value < 2:
        return False
    if value % 2 == 0:
        return False
    stop = math.sqrt(value)
    i = 3
    while i <= stop:
        if value % i == 0:
            return False
        i += 2
    return True

N = int(input())
for _ in range(N):
    print("Prime") if prime(int(input())) else print("Not prime")