import sys
from bisect import bisect_left

n,m = map(int,sys.stdin.readline().split())
data=[]

for _ in range(n):
  A = int(sys.stdin.readline().rstrip())
  data.append(A)
data.append(1000000000)
data.sort()

def binarySearch(data,target,start,end):
  while(start<=end):
    mid = (start+end)//2
    if target == data[mid]:
      return mid
    elif target > data[mid]:
      start = mid+1
    else:
      end = mid-1
  return -1

def leftIndex(data,d):
  left = bisect_left(data,d)
  if data[left] == d:
    return left  
  else:
    return -1

answer = []
for _ in range(m):
  d = int(sys.stdin.readline().rstrip())
  result = leftIndex(data,d)
  answer.append(result)

for i in answer:
  print(i)