def swap_case(s):
    res_string = ''
    for i in s:
        if i.isupper():
            res_string += i.lower()
        else:
            res_string += i.upper()
    return res_string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
