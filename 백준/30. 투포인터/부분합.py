input_num , target = map(int,input().split(" "))
num_list = list(map(int,input().split(" ")))

up_point = 0 # 총 합이 target보다 크면 하나 증가
down_point = 0 # 총 합이 target보다 작으면 하나 증가

total_sum =num_list[0]
min_len = 9999999
while True:
    if total_sum < target: # total_sum이 target보다 작을땐 down을 한칸 움직여 계산
        down_point += 1
        if down_point >= len(num_list): # 범위를 넘어갔을때
            break
        total_sum += num_list[down_point]
    else: # total_sum 이 target보다 크거나 같은경우(>=)up을 한칸 움직여 계산
        if up_point == down_point: # 하나로 target값을 만들 수 있는 경우
            min_len = 0
            break
        if up_point >= len(num_list): # 범위를 넘어갔을때
            break
        total_sum -= num_list[up_point]
        up_point += 1
    # 변경된 total_sum이 target보다 크냐 작냐 비교
    if total_sum >= target: # target보다 클때
        if min_len > (down_point - up_point):
            min_len = down_point - up_point
            
if min_len == 9999999:
    print(0)

else:
    print(min_len + 1)