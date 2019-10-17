# If you are sorting files by their size, the sizes need to stay connected to their respective files
# https://www.hackerrank.com/challenges/countingsort2/problem

def countingSort(arr):
    l = [0]* 100
    res = []
    for i in arr:
        l[i] += 1
    # l has the counts of each size 
    # next step: iterate the i size from 0 - 99
    # each size has l[i] counts so print the size and occurences. If there is no occurence then range (0,0)
    for i in range(0, 100):
        for j in range(0, l[i]):
            res.append(i)
    return res