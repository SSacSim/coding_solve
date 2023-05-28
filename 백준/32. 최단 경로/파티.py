
import heapq


N, M , X  = map(int,input().strip().split(" "))
matrix = []

matrix_dict = {}
for _ in range(M):
    input_list = list(map(int,input().strip().split(" ")))
    
    if input_list[0] not in matrix_dict:
        matrix_dict[input_list[0]] = [[input_list[1] , input_list[2]]] # 도착지점 , 거리
    else:
        matrix_dict[input_list[0]].append([input_list[1], input_list[2]])

# 다익스트라 x N 번
# 모든 정점에 대해 한번씩 봐야함..
answer = 0
for number in range(1,N+1):
    heap_list = []

    heapq.heapify(heap_list)
    s = number
    visit = [0 for _ in range(N + 1)] # 1 base
    inf = 9999999999
    memo = [inf for _ in range(N + 1 )] # 1base
    memo[s] = 0
    
    if visit[number] == 0 :
        heapq.heappush(heap_list, [0,s]) # 거리, 노드 
    flag = 0
    while len(heap_list) != 0:
        pop_ = heapq.heappop(heap_list) #가장 낮은 수 거리 pop 
        # pop_[0] = 최소거리 , pop_[1] = node 명
        if visit[pop_[1]] == 1 : # 이미 방문한 노드 skip
            continue
        visit[pop_[1]] = 1 # 방문 체킹
        
        # 연결된 node search and update
        for next_node in matrix_dict[pop_[1]] : # 연결된 노드 모두 확인하여 memo에 길이가 더 길면 update
            # next_node = 0: node name, 1 : length
            if memo[next_node[0]] > next_node[1] + memo[pop_[1]] :
                memo[next_node[0]] = next_node[1] + memo[pop_[1]]
                heapq.heappush(heap_list, [memo[next_node[0]] , next_node[0]]) # 거리, 노드 
            
        if flag == 0:
            memo[s] = inf
            flag += 1 
    
    if answer < memo[number]:
        answer = memo[number]
print(answer)