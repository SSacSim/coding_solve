import heapq
def solution(n, s, a, b, fares):
    # 1. start에서 시작하는 최단거리 다익스트라
    # 2. 각 node 다익스트라 계산 후 도착지점 거리 계산
    # 3. 모든 node 2번 과정을 거치며 최단거리 계산

    # matrix 인접리스트
    matrix = { i: [] for i in range(1,n+1)}

    # load insert

    for i in fares:
      matrix[i[0]].append([i[2] , i[1]]) # weight, to_node 
      matrix[i[1]].append([i[2] , i[0]]) # weight, to_node

    inf = 999999999
    
    def find_min_len(start_node):
      hq = []

      visit = [ 0 for _ in range(n + 1)] # 1 base 
      min_len = [ inf for _ in range(n + 1)] # 1 base 

      now_node = start_node
      visit[now_node] = 1
      min_len[now_node] = 0

      heapq.heappush(hq, [min_len[now_node],now_node]) # 시작 위치 넣기 [ len, node ]

      # 다익수행
      while len(hq) != 0 :

        # pop_ = [weight, node]
        pop_ = heapq.heappop(hq) # 최소값 node 뽑기
        #뽑았을 때, 방문한 것
        now_node_weight = pop_[0]
        now_node = pop_[1]
        visit[now_node] = 1

        # next node search and heap push
        for i in matrix[now_node] : # now_node와 연결된 next node search
          next_node = i[1]
          next_node_weight = i[0]
          # if min_len의 값보다 작으면 update
          if visit[next_node] == 0:
            if now_node_weight + next_node_weight < min_len[next_node]:
              min_len[next_node] = now_node_weight + next_node_weight

              # push heap
              heapq.heappush(hq, [min_len[next_node] , next_node])

      return min_len
    start_len = find_min_len(s) # 겹치는 부분 
    answer = inf
    for node_, i in enumerate(start_len[1:]):
      now_node = node_ + 1
      result = i# 해당 노드까지 중복으로 갔다고 가정 

      # 해당 노드부터 a,b 까지의 거리 구하자
      temp_len = find_min_len(now_node)
      result += temp_len[a]
      result += temp_len[b]
      if result < answer:
        answer = result
    return answer
