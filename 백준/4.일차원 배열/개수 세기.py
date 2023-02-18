number = int(input())

number_list = list(map(int,input().split(" ")))
target = int(input())
count = 0
for i in number_list:
  if i == target:
    count +=1
print(count)
