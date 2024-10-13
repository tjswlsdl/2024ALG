T = int(input())
anum = 0
bnum = 0

vote = list(str(input()))
for i in range(T):
    if vote[i] == 'A':
        anum += 1
    else :
        bnum += 1

if anum  == bnum :
    print('Tie')   
elif anum > bnum :
    print('A')
else:
    print('B')