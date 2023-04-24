# https://codeforces.com/gym/437545/problem/A



n = int(input())
nums = list(map(int, input().split()))

count = 0
result = 0
for i in range(n):
      if nums[i] >= nums[i-1]:
            count += 1
            result = max(result, count)
      else:
            count = 1
            
print(result)
