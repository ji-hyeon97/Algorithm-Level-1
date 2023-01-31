import sys

n = int(sys.stdin.readline().rstrip())
count = 0

for _ in range(n):
  data = sys.stdin.readline().rstrip()
  for i in range(len(data)-1):
    if data[i] == data[i+1]:
      continue
    else:
      if data[i] in data[i+1:]:
        count +=1
        break
        
print(n-count)
  
  
        
    

    
    
  