# https://www.hackerrank.com/challenges/sock-merchant/problem?h_r=next-challenge&h_v=zen#
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0 
    holder = []
    for i in ar: 
        holder.append(ar.count(i))
    holder = list(dict.fromkeys(holder))
    for j in holder:
        if j == 2:
            count += 1 
        elif j > 2:
            count += (j//2)
    return count 
    

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
