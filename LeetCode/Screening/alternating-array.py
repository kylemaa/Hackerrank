"""This function alternates the array from both ends and then check if altered array is ascending"""


def alternatingSort(a):
    n = len(a)
    b = []
    i = 0
    j = n-1
    while i < j:
        b.append(a[i])
        i += 1
        b.append(a[j])
        j -= 1
    # If start and end comes into the same index then add the num to the end of b array
    if i == j:
        b.append(a[i])
    k = 0
    while k < len(b)-1:
        if b[k] >= b[k+1]:
            return False
        k += 1
    return True
