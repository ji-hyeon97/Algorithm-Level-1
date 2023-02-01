import sys

n = int(sys.stdin.readline().rstrip())

distribute = []
for _ in range(n):
  weight = int(sys.stdin.readline().rstrip())
  distribute.append(weight)

distribute.sort(reverse=True)

answer = []
for i in range(1,n+1):
  case = i * distribute[i-1]
  answer.append(case)

print(max(answer))