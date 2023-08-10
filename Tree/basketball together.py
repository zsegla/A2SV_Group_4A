# https://codeforces.com/gym/437545/problem/C



n, d= map(int, input().split())
p= list(map(int, input().split()))
u= 0
p= sorted(p, reverse= True)

for j in p:
    if n > 0:
        for k in range(1, n+1):
            if k*j > d and n >= k:
                u += 1
                n -= k
                break
        else:
            break

print(u)
