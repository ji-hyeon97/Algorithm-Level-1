import sys

n = int(sys.stdin.readline().rstrip())
data =[]
k=1

for i in range(n):
  number = sys.stdin.readline().rstrip()
  data.append(number)

while(True):
  check = []
  for i in data:
    check.append(i[-k:])
  if len(data) == len(list(set(check))):
    print(k)
    break
  else:
    k+=1