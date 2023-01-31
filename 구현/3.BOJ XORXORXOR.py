import sys

a,b,c = map(int, sys.stdin.readline().split())

case = [a^b, (a^b)^b]
answer = 0

if c%2 == 1:
  answer = case[0]
else:
  answer = case[1]

print(answer)
