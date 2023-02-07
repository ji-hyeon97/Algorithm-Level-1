import sys

n = int(sys.stdin.readline().rstrip())

answer = 0
count = 0
for i in range(1,n+1):
  answer+=i
  count+=1
  if i >= n-answer:
    break
print(count)
  
  