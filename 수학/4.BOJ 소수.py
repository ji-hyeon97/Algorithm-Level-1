import sys

a,b,n = map(int, sys.stdin.readline().split())

data = a%b
up = 0
for _ in range(n):
  up = (data*10)//b
  data = (data*10)%b

print(up)