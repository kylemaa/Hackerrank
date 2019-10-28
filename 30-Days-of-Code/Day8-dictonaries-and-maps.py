# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input())
names_numbers = [input().split() for _ in range(n)]
phone_book = {k : v for k,v in names_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('{}={}'.format(name,phone_book[name]))
        else:
            print('Not Found')
    except:
        break