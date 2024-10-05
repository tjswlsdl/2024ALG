import sys
input = sys.stdin.readline

hour, min = map(int, input().split())
plus = int(input())

sum_min = min + plus

min_result = sum_min % 60
hour_result = (hour + int(sum_min / 60)) % 24


print(hour_result, min_result)