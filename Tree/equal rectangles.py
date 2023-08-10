# https://codeforces.com/gym/437545/problem/B



for cases in range(int(input())):
    n=int(input())
    ls=list(map(int,input().split()))
    ls.sort()
    area=ls[0]*ls[4*n-1]
    k=0
    for i in range(1,n+1):
        if(ls[2*i-2]==ls[2*i-1] and ls[4*n-2*i]==ls[4*n-2*i+1] and ls[2*i-2]*ls[4*n-2*i+1]==area):
            pass
        else:
            print('NO')
            k=1
            break
    if(k==0):
        print('YES')
