# https://codeforces.com/contest/1744/problem/D



t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))

    n2 = 0
    
    def pa(check, var):
        while check % 2 == 0:
            check //= 2
            var += 1
        return var

    for ii in a:
        n2 += pa(ii, 0)

    ans = n2

    if n2 >= n:
        print(0)
        continue

    b = [n - i for i in range(n)]

    c = []
    for i in range(n):
        val = 0
        while b[i] % 2 == 0:
            val += 1
            b[i] = b[i] // 2
        c.append(val)

    c = sorted(c, reverse=True)
    i = 0
    f = 0

    while i < n:
        if c[i] + ans >= n:
            print(i + 1)
            f = 1
            break
        else:
            ans += c[i]
            i += 1
    
    if f:
        continue

    print(-1)
