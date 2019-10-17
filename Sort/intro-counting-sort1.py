# https://www.hackerrank.com/challenges/countingsort1/problem
def countingSort(n, arr):
    l = [0]* 100
    for i in arr:
        l[i] += 1
    return l