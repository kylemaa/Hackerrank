# https://www.hackerrank.com/challenges/sock-merchant/problem?h_r=next-challenge&h_v=zen#
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    some_num = sum(ar.count(x)//2 for x in set (ar))
    return some_num 
    
    
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
