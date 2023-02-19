A,B = map(int,input().split(" "))
a_list = []
b_list = []

for i in range(A):
  a_list.append(list(map(int,input().split(" "))))
for i in range(A):  
  b_list.append(list(map(int,input().split(" "))))

answer = []
for i in range(len(a_list)):
  temp = []
  for j in range(len(a_list[0])):
    temp.append(a_list[i][j] + b_list[i][j])
  answer.append(temp)

for i in answer:
  print(*i)