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
    