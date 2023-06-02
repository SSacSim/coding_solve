import heapq
import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):

    n , d, c = map(int,input().strip().split(" ")) # 컴퓨터 갯수, 의존성 개수 , 해킹당한 컴퓨터
    matrix = {}

    for _ in range(d):
        input_temp = list(map(int,input().strip().split(" ")))
        
        if input_temp[1] not in matrix:
            matrix[input_temp[1]] = [ [input_temp[0], input_temp[2] ] ]
        else:
            matrix[input_temp[1]].append( [input_temp[0], input_temp[2] ] )

    heap_list  = []
    heapq.heappush( heap_list, [ 0 , c] ) # lenth, start

    inf = 9999999999
    memo = [ inf for _ in range(n + 1 )] # 1base
    visit = [ 0 for _ in range(n + 1 )] # 1base
    memo[c] = 0
    while heap_list:
        pop_ = heapq.heappop(heap_list) # length, start_node
        now_len = pop_[0]
        now_node = pop_[1]
        visit[now_node] = 1
        if now_node in matrix:
            for next_node in matrix[pop_[1]]: # next_node : node, length
                if visit[next_node[0]] == 0:
                    if next_node[1] + now_len < memo[next_node[0]] : 
                        memo[next_node[0]] = next_node[1] + now_len
                        heapq.heappush(heap_list, [ memo[next_node[0]] , next_node[0]])
        computer_count = 0
        computer_max = 0
        for i in memo:
            if i != inf:
                computer_count += 1 
                if computer_max < i:
                    computer_max = i      
    print(computer_count , computer_max)