from collections import deque
import sys
input = sys.stdin.readline

N , K = map(int,input().strip().split(" "))
visit = [0 for _ in range(100001)] # 최대 거리
memo = [-1 for _ in range(100001)] # 최대 거리

visit[N] = 1
memo[N] = -1 # 어디서 왔는지 체킹

my_q = deque([N])

while my_q:
    if visit[K] == 1:
        node_number = K
        node_list = []
        while True:
            if memo[node_number] == -1:
                node_list.append(node_number)
                break
            node_list.append(node_number)
            node_number = memo[node_number]
        
        print(len(node_list) - 1)
        print(*node_list[::-1])
        break
    now_location = my_q.popleft()
    
    # 3가지 우
    if now_location + 1 < len(visit) and visit[now_location + 1 ] == 0:
        visit[now_location + 1 ] = 1
        memo[now_location + 1] = now_location
        my_q.append(now_location + 1 )
    
    # 좌
    if now_location - 1 >= 0  and visit[now_location - 1  ] == 0:
        visit[now_location - 1  ] = 1
        memo[now_location - 1] = now_location
        my_q.append(now_location - 1  )
    
    # 순간이동
    if now_location * 2  < len(visit) and visit[now_location * 2 ] == 0:
        visit[now_location * 2  ] = 1
        memo[now_location * 2 ] = now_location
        my_q.append(now_location * 2 )
        