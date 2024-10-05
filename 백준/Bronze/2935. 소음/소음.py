#import sys
#input = sys.stdin.readline


a = int(input())
symbol = input()#.rstrip()
b = int(input())

result = 0

if symbol == '+':
    print(a+b)
elif symbol == '*' :
    print(a*b)