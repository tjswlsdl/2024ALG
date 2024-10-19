line = input()
stack=[]

cnt = 0

#막대기를 자른 횟수 + 1 = 조각 개수
#괄호 닫히는 순간이 자르는 순간인디,,
for i in range(len(line)):
    if line[i] == '(':
        stack.append('(')
        
    else: 
        if line[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        
        else: 
            stack.pop()
            cnt += 1
print(cnt)