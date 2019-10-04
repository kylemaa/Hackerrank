#https://www.hackerrank.com/challenges/bon-appetit/problem
# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    actual = (sum(bill) - bill[k]) / 2
    if actual == b:
        print('Bon Appetit')
    else:
        difference = abs(actual - b)
        print (difference)


    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)