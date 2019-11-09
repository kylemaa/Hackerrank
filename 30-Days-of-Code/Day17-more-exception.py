#Write your code here
class Calculator:
    def power(self, n, p):
        self.n = n
        self.p = p
        if self.n < 0 or self.p <0:
            raise Exception('n and p should be non-negative')
        else:
            return self.n ** self.p
        
    
T=int(input())
myCalculator = Calculator()
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 