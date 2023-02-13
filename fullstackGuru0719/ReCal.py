# this project is simple project
str = "asfj(sofke)skj(ss(sdf)(D)f)ffe"

def calc(str):
    
  if len(str) == 0:
    return s
  que = []
  ans = ""
  for i in range(len(str)):
    if str[i] == '(':
      que.append(i)
    elif str[i] == ')':
      if len(que) == 1:
        ans += calc(str[que[0] + 1 : i])[::-1]
      que.pop()
    else:
      if len(que) == 0:
        ans += str[i]
  return ans

print(calc(str))