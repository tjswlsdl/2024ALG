import sys
input = sys.stdin.readline

def create_tm(k):
    
    if k == 0 :
        return 0
    elif k == 1 :
        return 1
    else:
        if k % 2 == 0 :
            return create_tm(k//2)
        else:
            return 1-create_tm(k//2)
        
        

k = int(input())
print(create_tm(k-1))