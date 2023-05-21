def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks = [0] + rocks + [distance]
    
    temp_len = []
    for i in range(1,len(rocks)):
        temp_len.append(rocks[i] - rocks[i - 1])
    
    start = 0 #시작점
    end = distance # 종료지점 
    mid = (end + start) // 2
    
    answer = 0
    while True:
        mid = (end + start) // 2 # 중간지점

        lenth_sum = 0
        count = 0
        if start > end:
            break
        flag = 0
        for i in temp_len:
            if count > n: # 기준보다 많이 사용될때 mid가 낮아져야함
                flag = 1
                break

            lenth_sum += i

            if lenth_sum < mid:
                count += 1

            else:
                lenth_sum = 0
            if count > n: # 기준보다 많이 사용될때 mid가 낮아져야함
                flag = 1
                break

        if flag == 1:
            end = mid - 1 # mid보다 하나 작은것 까지
        else:
            answer = mid 
            start = mid + 1
            
    return answer