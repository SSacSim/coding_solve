N = int(input().strip())
num_list = []
for _ in range(N):
  num_list.append(int(input().strip()))
num_list.sort()

gap_list = []
for i in range(len(num_list) -1):
  gap_list.append(num_list[i+1] - num_list[i])

def gcd(a,b):
  while b != 0:
    a,b = b,a%b
  return a

temp = gcd(gap_list[0],gap_list[1])
answer = temp
for i in gap_list[2:]:
  temp = gcd(temp,i)
  answer = temp
    
count = ((num_list[-1] - num_list[0]) // answer + 1) - len(num_list)
print(count)
