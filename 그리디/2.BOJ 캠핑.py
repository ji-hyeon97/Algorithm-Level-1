import sys

count = 0
sequence = []
date = []

while(True):
  l,p,v = map(int, sys.stdin.readline().split())
  if l==0 and v==0 and p==0:
    break

  answer = l*(v//p) + min(l, v%p)
  count+=1
  
  sequence.append(count)
  date.append(answer)

for i in range(count):
    print("Case %d: %d" %(sequence[i], date[i]))