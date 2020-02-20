"""This function returns a mutated array given the formula a[i-1]+a[i]+a[i+1]"""


def mutateTheArray(n, a):
    b = []
    i = 0
    # Egde case
    if n == 1:
        return a
    while i < n:
        # Cover the start case
        if i == 0:
            b.append(a[i]+a[i+1])
        # Cover the end case
        elif i == n-1:
            b.append(a[i-1]+a[i])
        # Normal case
        else:
            b.append(a[i-1]+a[i]+a[i+1])
        i += 1
    return b


print(mutateTheArray(4, [1, 2, 3, 5]))
