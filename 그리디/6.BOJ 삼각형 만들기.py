import sys

n = int(sys.stdin.readline().rstrip())
lines = []

for _ in range(n):
  line = int(sys.stdin.readline().rstrip())
  lines.append(line)

lines.sort(reverse = True)

answer = 0
possible = 1
for i in range(len(lines)-2):
  if lines[i] < lines[i+1] + lines[i+2]:
    answer = lines[i] + lines[i+1] + lines[i+2]
    possible = 1
    break
  else:
    possible = 0

if possible ==1:
  print(answer)
else:
  print(-1)