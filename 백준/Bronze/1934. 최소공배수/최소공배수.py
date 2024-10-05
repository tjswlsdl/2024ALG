import sys
#import numpy as np
input = sys.stdin.readline

T = int(input())
lst = []
x = 1

for i in range(T):
    a, b = map(int, input().split())
    
    for j in range(min(a,b),0,-1): 
        if (a % j == 0) and (b % j == 0):
            x = j
            break
            
    result = int(a*b / x)
    print(result)