def Rev(x):
    x=x[::-1]
    return  x


a,b = map(str, input().split())
result = str(int(Rev(a)) + int(Rev(b)))

print(int(Rev(result)))