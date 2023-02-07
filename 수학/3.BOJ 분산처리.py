# python3에서는 시간초과 발생 pypy3는 통과 (n^2인데 pypy3에서는 우찌 통과된거징 ?? t값의 범위가 안주어졌긴 하지만 ....)
import sys

t = int(sys.stdin.readline().rstrip())

answer = 1
result = []
for _ in range(t):
  a,b = map(int, sys.stdin.readline().split())
  for _ in range(b):
    if (answer*a)%10 == 0:
      answer = 10
    else:
      answer = (answer*a)%10
  result.append(answer)
  answer = 1

for i in result:
  print(i)