n = 6

vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

node_visit = [-1] * (n + 1) # 1 base

node = dict()

for i in vertex:
    start, end = i[0] , i[1]
    if start not in node:
        node[start] = [end]
    else:
        node[start].append(end)
        
    if end not in node:
        node[end] = [start]
    else:
        node[end].append(start)
    
    
print(node)

#bfs 
from collections import deque

my_que = deque([[1,0]]) # node번호, 총 간선 수 ,node_visit
node_visit[1] = 0
max_count = 0
max_count_num = 0
while True:
    print(my_que)
    print("==========================")    

    if len(my_que) == 0:
        break
    
    now_node, edge_count = my_que.popleft()
    
    for indx, j in enumerate(node[now_node]):
        print("j",j)
        
        if node_visit[j] == -1  :
            my_que.append([j,edge_count + 1])
            node_visit[j] = edge_count + 1
            if (edge_count + 1) > max_count:
                    max_count = edge_count + 1
                    max_count_num = 1
            elif (edge_count + 1) == max_count:
                max_count_num += 1


print(max_count)
print(max_count_num)