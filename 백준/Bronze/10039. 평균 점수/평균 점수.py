import sys
#import numpy as np
input = sys.stdin.readline

lst = []
sum = int(0)


for _ in range(5):
    score = int(input())
    lst.append(score)
    
for i in range(5):
    if lst[i] >= 40 :
        sum = sum + lst[i]
    else :
        sum = sum + 40
        
print(int(sum/5))

