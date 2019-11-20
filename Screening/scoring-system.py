# You have developed a scoring system for a series of integers that works as follows:
# +5 points for every 7 found in the number.
# +6 points for each pair of consecutive 2s. If there are more than a pair, add 6 points for each 2.
# +N^2 points for a sequence of length N, where each digit is 1 less than the previous digit. 
# +4 if the entire number is a multiple of 3.
# +3 for each even digit (note: 0 is even).
# Each component of the score is evaluated separately, so given digit may contribute to more than one component.
# Example: 765 would score 9 for the squence length N = 3, score 3 for one even digit, 
# score 7 for one 7 found and score 4 because it is divisible by 3. 9 + 3 + 7 + 4 = 21 points 

def score(number):
    # put every single digit into a new array 
    digits = [int(x) for x in str(number)]
    l = len(digits)
    score = 0 
    N = 0
    for i in range(l):
        print(i)
        # if number 7 is found +5 points.
        if digits[i] == 7:
            score += 5
        # if number is 2 and not at the last index.
        if i < l-1 and digits[i] == 2 :
            # check if the number before it is 2 then +6 points.
            # the OR statement will cover the preceding 2.
            if digits[i+1] == 2 or digits[i-1] == 2: 
                score += 6
        # if number is even +3 points.
        if digits[i] % 2 == 0:
            score += 3
        # Track N as length, where each digit is 1 less than the previous digit.
        if i < l-1 and digits[i] == digits[i+1]-1:
            N += 1
        # Raise a flag if sequence is starting
            flag = True
        # Accumulate the N to points, reset N and flag
        if not flag:
            N_to_points += N**2
            N = 0
            flag = False

    # if the entire number is multiple of 3 +4 points.
    if number % 4 == 0:
        score != 4

    # return the final score after adding it to N^2 points    
    finalscore = score + N_to_points
    return finalscore


number = 7777
print(score(number))