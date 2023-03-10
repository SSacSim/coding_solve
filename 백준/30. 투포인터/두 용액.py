N = int(input())
num_list = list(map(int,input().strip().split(" ")))
num_list.sort()
left_point = 0
right_point = len(num_list) - 1


#더해서 음수가 나오면, left point 증가
#더해서 양수가 나오면, right point 감소
result_left = 0
result_right = 0
total_min = 999999999999999999999
while True:
    if left_point >= right_point:
        break
    
    if abs(num_list[left_point] + num_list[right_point]) < total_min:
        total_min = abs(num_list[left_point] + num_list[right_point])
        result_left = num_list[left_point]
        result_right = num_list[right_point]

    if num_list[left_point] + num_list[right_point] > 0:
        right_point -=1
    elif num_list[left_point] + num_list[right_point] < 0:
        left_point +=1
    else:
        break
print(result_left , result_right)