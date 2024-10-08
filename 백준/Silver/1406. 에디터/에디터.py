#https://corin-e.tistory.com/entry/%EB%B0%B1%EC%A4%80-1406-%EC%97%90%EB%94%94%ED%84%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from sys import stdin

left = list(input())
right = []

for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == 'L' and left:
        right.append(left.pop())
    elif command[0] == 'D' and right:
        left.append(right.pop())
    elif command[0] == 'B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

answer = left + right[::-1]
print(''.join(answer))
#출처: https://corin-e.tistory.com/entry/백준-1406-에디터-파이썬 [🪨 🪨 🪨:티스토리]