import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline().rstrip())
answer = []

for i in range(1,n+1):
  queue.append(i)

while(True):
  if len(queue) ==0:
    break
  answer.append(queue.popleft())
  if len(queue) ==0:
    break
  second = queue.popleft()
  queue.append(second)

for i in answer:
  print(i, end=" ")
