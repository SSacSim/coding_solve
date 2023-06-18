#... how to..?? dfs? bfs??
#=================== not solved ========
from collections import deque

T = int(input())
for _ in range(T) :
    A , B = map(int,input().strip().split(" "))

    # 방문 저장 
    visit = [0  for _ in range(10000)]

    my_q = deque([[ A, "" ]]) # 현재 값 , route

    while my_q :
        now_value , now_route = my_q.popleft() # 1234 , ""
        if now_value == B:
            print(now_route)
            break
        # 현재까지 길이가 저장된 길이보다 길다면 continue
        if visit[now_value] == 1:
            continue
        # 4가지 방식 존재
        # 1. D > x2
        # 2. S > -1 ,0 처리
        # 3. L > 
        # 4. R > 
        new_value = (now_value * 2) % 10000
        my_q.append([new_value , now_route+"D"])
    
        if now_value == 0:
            my_q.append([9999 , now_route+"S"])
        else:
            my_q.append([now_value - 1 , now_route+"S"])
            
        # L
        cal = now_value % 10**(len(str(now_value)) - 1) * 10 + now_value // 10**(len(str(now_value)) - 1)
        my_q.append([cal , now_route+"L"])
        visit[cal] = 1
        
        # R
        cal = now_value % 10 * 10**(len(str(now_value))-1) +now_value // 10
        my_q.append([cal , now_route+"R"])
        visit[cal] = 1
