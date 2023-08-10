# https://codeforces.com/gym/437545/problem/D



n, m = map(int, input().split())
d = 0
k = 0
if m%n != 0:
    print(-1)
else:
    d = m//n
    while d!= 1:
        if d %2 == 0:
            d =d//2
            k+=1
        elif d%3 == 0:
            d = d // 3
            k += 1
        else:

            d = 1
            k = -1
    print(k)



