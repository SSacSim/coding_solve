tickets = 	[["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]
# dfs로 풀어야함.

tickets_len = len(tickets)

from copy import deepcopy

visit_map = dict()
for i in tickets:
    start , end = i[0] , i[1]
    if start not in visit_map:
        visit_map[start] = [[end , 1]]
    else:
        visit_map[start].append([end,1])

for i in visit_map:
    visit_map[i].sort()
print(visit_map)

# dfs로 풀이

start_node = "ICN"
visit_node=["ICN"]
my_answer = 0
def dfs(start_node,visit_node_1,visit_map_1,flag):
    print("dfs")
    print("start node",start_node)
    print("visit_node",visit_node_1)
    print(flag)
    if flag == 1:
        print("falg 실행")
        return 1
    if len(visit_node_1) == tickets_len + 1:
        print("저장!!!!!!!!!")
        global my_answer
        my_answer = visit_node_1
        print(visit_node_1)
        # flag return
        return 1
    
    if (flag == 0) and (start_node in visit_map_1):
        for index, i in enumerate(visit_map_1[start_node]):
            '''
            i = [next node, 남은 수] 
            '''
            print("i", i )
            next_node , leave_count= i
            if leave_count == 1 :
                tmep_visit_map = deepcopy(visit_map_1)
                
                temp_visit_node = deepcopy(visit_node_1)
                temp_visit_node.append(next_node)
                
                tmep_visit_map[start_node][index][1] = 0
                print('visit_map' ,visit_map_1)
                print("next_node, visit_node",next_node,temp_visit_node)
                print("=====================")
                flag = dfs(next_node,temp_visit_node,tmep_visit_map , flag)
                if flag == 1:
                    break
                print("======dfs 탈출=========")
    if flag == 1:
        return 1
    else:
        return 0
dfs(start_node, visit_node,visit_map ,0)

print(my_answer)