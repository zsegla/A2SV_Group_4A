# https://codeforces.com/problemset/problem/1675/D



def f():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print('1' + "\n" + '1' + "\n" + '1' + "\n")
        return
    visited = [False] * n
    branch = [True] * n
    for i in a:
        branch[i-1] = False
    print(branch.count(True))
    for i in range(n):
        if branch[i]:
            t = i
            path = [i+1]
            while not visited[a[t]-1]:
                visited[a[t]-1] = True
                path.append(a[t])
                t = a[t]-1
            print(len(path))
            print(' '.join(str(x) for x in path[::-1]))
    print()



for _ in range(int(input())):
    f()
