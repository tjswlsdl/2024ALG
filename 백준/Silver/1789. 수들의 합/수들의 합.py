import sys
#import numpy as np
input = sys.stdin.readline


N_max = int(input())

sum = 0

if N_max == 1 :
    print(1)
elif N_max == 2 :
    print(1)
else:
    for i in range(1, N_max):
        sum = sum + i
        if sum > N_max:
            result = i-1
            print(result)
            break
        elif sum == N_max:
            result = i
            print(result)
            break