import sys
from bisect import bisect_left, bisect_right

n,m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

def biggerSame(value):
  result = bisect_left(data,value)
  print(len(data)-result)

def bigger(value):
  result_right = bisect_right(data,value)
  print(len(data)-result_right)

def belongs(start, end):
  result_left = bisect_left(data,start)
  result_right = bisect_right(data,end)
  print(result_right - result_left)
  
for _ in range(m):
  case = list(map(int, sys.stdin.readline().split()))
  if case[0] == 1:
    biggerSame(case[1])

  if case[0] == 2:
    bigger(case[1])

  if case[0] == 3:
    belongs(case[1],case[2])
    