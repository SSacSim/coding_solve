# 시간 복잡도와 공간 복잡도를 고려한 문제
# 공간 복잡도를 줄이기 위해선, Q에 이동 경로 데이터를 넣으면 안됨.
# 하나의 memo 공간을 이용하여 역 추적하는 방식을 사용해야함.
import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    
    A, B = map(int,input().strip().split(" "))
    my_q = deque([ A ]) # 현재 숫자, 어디서부터 왔는지 


    visit = [ 0 for _ in range( 10001)]
    visit[A] = 1
    # 이전 어떤 작업을 통해 해당 수까지 올 수 있었는지 기록 
    memo = [ [] for _ in range(10001)] 

    while my_q:
        # print("-----")
        # print(my_q)
        
        # pop_ number 
        now_number = my_q.popleft()
        
        if now_number == B:
            break
        
        # D - 2배
        change_num = ( now_number * 2 ) % 10000
        if visit[change_num] == 0:
            visit[change_num] = 1
            if memo[change_num] ==[]:
                memo[change_num].append(now_number)
                memo[change_num].append("D")
            my_q.append(change_num)
            
        # S - -1
        #print(now_number)
        change_num = now_number
        if now_number == 0:
            change_num = 9999
        else:
            change_num -= 1
            
        if visit[change_num] == 0:
            visit[change_num] = 1
            if memo[change_num] ==[]:
                memo[change_num].append(now_number)
                memo[change_num].append("S")
            my_q.append(change_num)
        
        # L - left shift
        change_num = now_number
        change_num = ((change_num // 1000)  + (change_num % 1000) * 10 )
        if visit[change_num] == 0 :
            visit[change_num] = 1
            if memo[change_num] ==[]:
                memo[change_num].append(now_number)
                memo[change_num].append("L")
            my_q.append(change_num)
            
        # R - right shift
        change_num = now_number
        change_num = ((change_num % 10) * 1000 + (change_num // 10) )
        if visit[change_num] == 0 :
            visit[change_num] = 1
            if memo[change_num] ==[]:
                memo[change_num].append(now_number)
                memo[change_num].append("R")
            my_q.append(change_num)
# 역추적
    result = ""
    now_ = B
    while True:
        result += memo[now_][1]
        
        if memo[now_][0] == A:
            break
        
        now_ = memo[now_][0]
    print(result[::-1])
