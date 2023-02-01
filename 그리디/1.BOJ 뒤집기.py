import sys

s = sys.stdin.readline().rstrip()
s += "4"
data = []
one = 0
zero = 0
answer = 0

for i in range(len(s)-1):
  if s[i] != s[i+1]:
    data.append(s[i])

if(len(data))==1:
  answer = 0
  
else:
  for i in data:
    if i=='0':
      zero+=1
    elif i=='1':
      one+=1
  answer = min(zero,one)
print(answer)