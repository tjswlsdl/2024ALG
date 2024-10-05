import sys
input = sys.stdin.readline


a = int(input())
symbol = input().rstrip()
b = int(input())

result = 0

if symbol == '+':
    result = a+b
elif symbol == '*' :
    result = a*b

    
print(result)