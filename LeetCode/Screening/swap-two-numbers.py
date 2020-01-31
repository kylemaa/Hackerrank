def swapTwoDigits(n):
    n_list = list(str(n))
    l = len(n_list)
    i = 0
    ret_s = ''
    while i < l-1:
        n_list[i], n_list[i+1] = n_list[i+1], n_list[i]
        i += 2
        if i == l-2 and l % 2 == 1:
            break
    for i in range(l):
        ret_s += n_list[i]
    return int(ret_s)


n = 123456
print('Expected: 214365')
print('Result:', swapTwoDigits(n))
