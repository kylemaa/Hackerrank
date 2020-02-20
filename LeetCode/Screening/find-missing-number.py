# Given an array A of N integers, return that smallest positive integer that does not occur in A.


def solution(A):
    # Eliminate duplicates and sort the array
    A = set(sorted(A))
    number = 0
    for i in A:
        if i > 0 and i == number+1:
            number = i
        elif i != number + 1:
            return number + 1
    return number+1


A = [1, 3, 6, 4, 1, 2]  # Expect 5

B = [1, 2, 5, 4]  # Expect 3

C = [1, 2, 3]  # Expect 4
print(solution(C))
