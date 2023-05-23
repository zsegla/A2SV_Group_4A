# https://www.eolymp.com/en/contests/9060/problems/78597



n = int(input())

roads = 0
for _ in range(n):
    row = list(map(int, input().split()))
    roads += sum(row)

roads //= 2

print(roads)
