import sys
import math
input = sys.stdin.readline


song_num, avg = map(int, input().split())
min_avg = avg - 0.99 

result = math.ceil(song_num * min_avg)


print(result)