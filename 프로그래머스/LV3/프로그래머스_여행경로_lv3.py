tickets = 	 [['ICN','A'],['A','B'],['A','C'],['B','A'],['C','A']]

tickets_len = len(tickets)
# 방문 map (array로 변경)

from collections import deque
from copy import deepcopy

visit_map = dict()
for i in tickets:
    start , end = i[0] , i[1]
    if start not in visit_map:
        visit_map[start] = [[end , 1]]
    else:
        visit_map[start].append([end,1])

print(visit_map)

my_que = deque([["ICN",["ICN"], visit_map]]) #반드시 ICN에서 출발 // #지금 출발 공항 / 지금까지 거쳐온 공항 / 남은 티켓
 

answer = []
while True:
    print(my_que)
    if len(my_que) == 0:
        break
    
    '''
    str , list ["INC","IAW"...], list ['ICN': [['JFK', 1]] ]
    '''
    now_port , history_port, leave_ticket = my_que.popleft()
    
    if len(history_port) == tickets_len + 1:
        if history_port not in answer:
            answer.append(history_port)
        
    print("now_port " , now_port )
    print("history_port", history_port)
    print("leave_ticket" , leave_ticket)
    if now_port in leave_ticket: # 갈수 있는 곳이 있을때 
        for index, i in enumerate(leave_ticket[now_port]): # 현 포트에서 갈 수 있는 곳 
                print(i)
                print("***********************")
                if i[1] == 0: # 갈수 있는 곳은 있지만 티켓이 남아있지 않을때 
                    continue
                
                print( leave_ticket[now_port])
                print( leave_ticket[now_port][index])
                print( leave_ticket[now_port][index][1])
                print("*******222**********")
                temp_leave = deepcopy(leave_ticket)
                temp_leave[now_port][index][1] = 0 #방문했으니 0으로 처기화
                
                print(temp_leave)
                print("*******33333**********")
                my_que.append([i[0],history_port + [i[0]] , temp_leave])

    print("after que ", my_que)
    print("==================================")

print(answer)
answer.sort()
print(answer[0])