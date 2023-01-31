import sys
from collections import Counter

data = sys.stdin.readline().rstrip()
answer = 0
six_nine = []
others = []

stuff = Counter(data).most_common()

for i in range(len(stuff)):
  if stuff[i][0] == '6' or stuff[i][0] == '9':
    six_nine.append(int(stuff[i][1]))

  else:
    others.append(int(stuff[i][1]))
    
if len(six_nine) == 0:
  SIX_NINE = 0
else:
  SIX_NINE = sum(six_nine)
  
if len(others) == 0:
  OTHERS = 0
else:
  OTHERS = max(others)

if SIX_NINE > OTHERS:
  if SIX_NINE%2 == 1:
    answer = int(SIX_NINE//2) + 1
  else:
    answer = SIX_NINE//2
else:
  answer = OTHERS
  
print(answer)
