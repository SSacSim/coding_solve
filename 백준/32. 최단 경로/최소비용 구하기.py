import sys
import heapq

heap_list = []
heapq.heapify(heap_list)

input =sys.stdin.readline
N = int(input())
M = int(input())

to_dict = {} 
for _ in range(M):
    input_ = list(map(int,input().strip().split(" ")))
    
    if input_[0] not in to_dict:
        to_dict[input_[0]] = [[input_[1] , input_[2]]]
    else:
        to_dict[input_[0]].append([input_[1] , input_[2]])
s ,e = map(int,input().strip().split(" "))
inf = 99999999
visit = [ 0 for _ in range(N + 1 )]# 1 base 
min_len = [ inf for _ in range(N + 1 )]# 1 base
min_len[s] = 0

while True:
    # 방문 체킹! 
    if sum(visit) == N:
        break
    visit[s] = 1
    if s in to_dict:
        for i in to_dict[s]:
            if min_len[s] + i[1] < min_len[i[0]]: # 기존에 있는 거리보다 작을때
                min_len[i[0]] = min_len[s] + i[1]
                heapq.heappush(heap_list,[min_len[i[0]], i[0]]) # 최단거리 , 노드 
    if len(heap_list) == 0:
        break
    while len(heap_list) !=0 :
        temp = heapq.heappop(heap_list) # 다음 노드 찾기 ( 최단거리 인것 )
        next_s = temp[1]
        if visit[next_s] == 0 :
            s = next_s
            break     

print(min_len[e])
