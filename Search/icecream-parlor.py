# https://www.hackerrank.com/challenges/icecream-parlor/problem
def icecreamParlor(money, costs):
    h = dict()
    for i, cost in enumerate(costs):
        h[cost] = i
    for i, cost in enumerate(costs):
        complement = money - cost 
        if complement in h:
            if h[complement] != i:
                return sorted([h[complement]+1, i+1])
