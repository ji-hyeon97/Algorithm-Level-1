import sys

t = int(sys.stdin.readline().rstrip())

answer = 0
result = []
for _ in range(t):
  move = list(map(int, sys.stdin.readline().split()))
  n = int(sys.stdin.readline().rstrip())
  for _ in range(n):
    circle = list(map(int, sys.stdin.readline().split()))

    if (circle[0] - move[0])**2 + (circle[1] - move[1])**2 <= circle[2]*circle[2] and (circle[0] - move[2])**2 + (circle[1] - move[3])**2 >= circle[2]*circle[2]:
      answer+=1

    if (circle[0] - move[0])**2 + (circle[1] - move[1])**2 >= circle[2]*circle[2] and (circle[0] - move[2])**2 + (circle[1] - move[3])**2 <= circle[2]*circle[2]:
      answer+=1
    
  result.append(answer)
  answer = 0

for i in result:
  print(i)

    
      
    


      