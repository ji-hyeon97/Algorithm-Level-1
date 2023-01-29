import sys

x,y = map(int, sys.stdin.readline().split())
while(True):
  if x%10 == 0:
    x = x//10
    continue
    
  if y%10 ==0:
    y = y//10
    continue
  break
  
x = str(x)
y = str(y)
newX = ""
newY = ""
for i in range(len(x)):
  newX +=x[len(x)-i-1]
for i in range(len(y)):
  newY +=y[len(y)-i-1]

newX  = int(newX)
newY = int(newY)

data = newX+newY
data = str(data)

answer=""
for i in range(len(data)):
  answer += data[len(data)-i-1]

answer = int(answer)

print(answer)