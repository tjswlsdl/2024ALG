# -*- coding: utf-8 -*-
import sys
from collections import deque
import heapq
import bisect
import math
from itertools import product
from itertools import combinations
"""
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
import copy
"""
#input=sys.stdin.readline
#print=sys.stdout.write
#sys.setrecursionlimit(100000000)

n=int(input())
D={}
L=[]
ans=0
for i in range(n):
    a,b=input().rstrip().split()
    x=a[:2]+b
    if x not in D:
        D[x]=1
    else:
        D[x]+=1
    L.append((a[:2],b))
for i in range(n):
    if L[i][0]==L[i][1]:
        continue
    if L[i][1]+L[i][0] in D:
        ans+=D[L[i][1]+L[i][0]]
print(ans//2)