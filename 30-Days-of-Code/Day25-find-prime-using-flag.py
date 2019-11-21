import math
T=int(input())
for i in range(T):
    n=int(input())
    flag=True
    if n==1:
        flag=False
    if n==2:
        flag=True
    for j in range(2,int(math.sqrt(n))+1):
        if n%j==0:
            flag=False
            break
    if flag==True:
        print("Prime")
    else:
        print("Not prime")