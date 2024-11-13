N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = a + a
if " ".join(map(str, b)) in " ".join(map(str, a)):
    print("YES")
else:
    print("NO")