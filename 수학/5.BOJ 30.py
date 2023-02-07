import sys

n = int(sys.stdin.readline().rstrip())
data = str(n)

total = 0
while(True):
  if '0' not in data:
    print(-1)
    break
    
  for i in data:
    total+=int(i)
  if total %3 != 0:
    print(-1)
    break
      
  answer = []
  for i in data:
    answer.append(int(i))

  answer.sort(reverse = True)
  result = ''
  for i in answer:
    result+= str(i)
  print(int(result))
  break