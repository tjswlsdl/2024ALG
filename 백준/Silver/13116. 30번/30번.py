for _ in range(int(input())) :
    a, b = map(int, input().split())
    if a > b : a, b = b, a
    a_lst = []
    b_lst = []
    while a > 0 :
        a_lst.append(a)
        a //= 2
    while b > 0 :
        if b in a_lst :
            print(b * 10)
            break
        b //= 2
#출처: https://woongtech.tistory.com/entry/BOJ백준-13116-30번-Cpython [WOONGTECH:티스토리]