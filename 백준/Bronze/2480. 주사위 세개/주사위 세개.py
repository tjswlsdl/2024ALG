import sys
#import numpy as np
input = sys.stdin.readline

dice = list(map(int, input().split()))
lst = []
x=1

if (len(set(dice))) == 3:
    print(max(dice) * 100)

elif (len(set(dice)) == 2):
    for i in dice:
        if i not in lst:
            lst.append(i)
        else :
            x = i
    print(x*100 + 1000)
    
else : 
    print(dice[0]*1000+ 10000)





