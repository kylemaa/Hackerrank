# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

def hackerlandRadioTransmitters(x, k):
    transmitter = 0
    i = 0 
    while i < (len(x)):
        transmitter += 1
        next_point = x[i]+k 
        while (i< len(x) and x[i] <= next_point):
            i += 1
        next_point = x[i-1]+k
        while (i< len(x) and x[i]<= next_point):
            i += 1 