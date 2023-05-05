N = int(input())
num_list = [0 ,1]
for i in range(N):
  num_list.append(num_list[i] + num_list[i+1])
print(num_list[N])
