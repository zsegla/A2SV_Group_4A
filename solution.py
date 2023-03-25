def solution (security_code, key_pad):
  hashm = {}
  securityC = list(security_code)
  keyP = list(key_pad)
  for i,num in enumerate(keyP):
    hashm[num] = i  
  
  time = 0
  stack = []
  for num in securityC:
    while stack[-1] and stack[-2]:
      l = stack.pop()
      r = stack.pop()
      diff = r - l
      if diff == 1 or diff == 2 or diff == 3:
        time += 1
      elif diff == 6:
        time += 2
      else :
        time += 0
    stack.append(num)
  return time 
