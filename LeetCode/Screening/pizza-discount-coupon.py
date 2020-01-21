# Nutanix assessment


def solve(N, days):
    # Write your code here
    left_over = 0
    for v in range(N):
        # on the days with even visitors, I can use discount minus the left-over from the odd days
        # edge case when there is no visitors and there is left_over then return False
        if days[v] == 0 and left_over != 0:
            break
        # calculate the total pizzas of the day
        pizzas = abs(days[v] - left_over)
        # set the left_over to zero if pizzas I have to order is even
        if pizzas % 2 == 0:
            left_over = 0
        # set the left_over from the odd days
        elif pizzas % 2 == 1:
            left_over = pizzas % 10
    # If reach the end of array and I don't have total equates to 0 then return False else True
    if left_over == 0:
        print('YES')
    else:
        print('NO')


N = int(input())
days = [int(i) for i in input().split()]

solve(N, days)
