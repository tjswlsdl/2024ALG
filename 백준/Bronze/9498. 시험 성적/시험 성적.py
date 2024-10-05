SCORE = input()
SCORE = int(SCORE)

if SCORE<0 or SCORE>100:
    print('다시입력하세요 : ')
elif 90 <= SCORE <= 100:
    print('A')
elif 80 <= SCORE <= 89:
    print('B')
elif 70 <= SCORE <= 79:
    print('C')
elif 60 <= SCORE <= 69:
    print('D')
else:
    print('F')