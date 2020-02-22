# https://www.geeksforgeeks.org/python-get-all-substrings-of-given-string/


def substringString(S):
    return [S[i:j]for i in range(len(S)) for j in range(i+1, len(S)+1)]


def substringList(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            result.append(arr[i:j])
    return result


sample = "Geeks"
print(substringString(sample))
print(substringList(sample))
