def findLongestSequence(seq):
    # egde case 
    if len(seq) < 2:
        return len(seq)
    # keep track of the first two numbers of sequence
    a, b = seq[0], seq[1]
    last_num = b
    last_num_count = 1 if (a == b) else 0
    length = 1
    max_length = 1 

    for n in seq[1:]:
        # if n is either a or b then length +1 
        if n in (a, b):
            length += 1
            # if current num is equal to last num, +1 count in case of same number
            if n == b:
                last_num_count += 1
            # else last num will be reassigned to a     
            else:
                last_num = a
                last_num_count = 1
        else:
            # pass last number to a,  and current num to b, last_num now holds the second number that makes the seq
            a = last_num 
            b = n
            last_num = b
            # pass the length of last num count to current length and reset the last num count 
            length = last_num_count + 1
            last_num_count = 1
        max_length = max(length, max_length)
    return max_length

print(findLongestSequence([1, 3, 5, 3, 1, 3, 1, 5]))
print(findLongestSequence([1, 1, 3, 3, 4, 4]))


    