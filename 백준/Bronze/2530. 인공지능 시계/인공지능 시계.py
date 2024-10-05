import sys
input = sys.stdin.readline

hour, min, sec = map(int, input().split())
plus = int(input()) #걸리는 시간(초단위)

sum_sec = sec + plus
sum_min = min + sum_sec // 60

sec_result = sum_sec % 60
min_result = (min + sum_sec // 60) % 60
hour_result = (hour + sum_min // 60) % 24 # // = 몫 반환 메모리 더쓰긴함 ㅋㅋ



print(hour_result, min_result , sec_result)