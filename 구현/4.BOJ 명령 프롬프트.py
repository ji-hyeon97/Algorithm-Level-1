import sys

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n)]
length = 0
answer = ""

for i in range(n):
  data = sys.stdin.readline().rstrip()
  length = len(data)
  for j in range(len(data)):
    graph[i].append(data[j])

check = []
for i in range(length):
  for j in range(n):
    check.append(graph[j][i])
  if len(list(set(check))) == 1:
    answer+=check[0]
  else:
    answer+="?"
  check=[]

print(answer)
    


  
  
  
  
        
    

    
    
  