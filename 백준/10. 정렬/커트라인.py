total_num, target = map(int,input().split(" "))
num_list = list(map(int,input().split(" ")))
num_list.sort(reverse = True)
print(num_list[target - 1])
