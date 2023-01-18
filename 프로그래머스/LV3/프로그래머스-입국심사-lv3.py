n = 7
times = [10, 10]

end = max(times) * n
start = 0

answer = 0
while True:
    count = 0 # 해당 시간이 주어졌을때 총 몇명의 고객을 맞이할 수 있는가
    mid = (end - start) //2 + start
    print("start",start)
    print("end",end)
    print("mid",mid)
    if start > end :
        break
    for i in times:
        count += mid // i
    
    print("count",count)
    # target n보다 더 적은 수를 맞이할때 > 시간을 늘려야함
    if  count < n:
        start = mid + 1
    
    elif count >= n:
        end = mid -1

    if count >= n:
        answer = mid
    print("==================")

print(answer)