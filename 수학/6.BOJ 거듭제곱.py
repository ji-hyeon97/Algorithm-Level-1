import sys

n = int(sys.stdin.readline().rstrip())
data = bin(n).replace('0b',"")
number = data[::-1]

answer = 0
for i in range(len(number)):
  if number[i] == '1':
    answer+=3 ** i
print(answer)