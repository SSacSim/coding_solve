n = int(input())
num_list = list(map(int,input().split(" ")))
temp_0 = num_list.copy()
num_array = []
num_array.append(num_list)
num_array.append(temp_0)
global_max = num_array[0][0]
for index, i in enumerate(num_array[0]):
  for j in range(index):
    if num_array[0][index] > num_array[0][j] : 
      if num_array[1][index] < num_array[0][index] + num_array[1][j]:
        num_array[1][index] = num_array[0][index] + num_array[1][j]
        if global_max < num_array[1][index]:
          global_max = num_array[1][index]
print(global_max)
