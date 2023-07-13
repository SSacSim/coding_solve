import sys
input = sys.stdin.readline

N = int(input().strip())
memo_ = {}
visit = [ 0 for _ in range(N + 1)] # 1 base 
flag = [ 0 for _ in range(N + 1)] # 1 base
for _ in range(N-1):
    temp = list(map(int,input().strip().split(" ")))
    
    if temp[0] not in memo_:
        memo_[temp[0]] = [temp[1]]
    else:
        memo_[temp[0]].append(temp[1])
        
    if temp[1] not in memo_:
        memo_[temp[1]] = [temp[0]]
    else:
        memo_[temp[1]].append(temp[0])
    
from collections import deque

my_q = deque([1])# 
visit[1] = 1 

while my_q:
    parent_node = my_q.popleft()

    for next_node in memo_[parent_node]:
        if visit[next_node] != 1 :
            visit[next_node] = 1
            flag[next_node] = parent_node
            my_q.append(next_node)
        
for i in range(2,len(flag)):
    print(flag[i])
