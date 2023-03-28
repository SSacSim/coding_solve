number = int(input())
num_list = list(map(int,input().split(" ")))
target = int(input())
num_list.sort()
point_left = 0
point_right = len(num_list) -1
count = 0
while True:
  if point_left >= point_right:
    break
  
  if num_list[point_left] + num_list[point_right] > target:
    point_right -= 1
  elif num_list[point_left] + num_list[point_right] < target:
    point_left += 1
  else:
    count +=1
    point_left +=1
print(count)