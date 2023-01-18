user_id =  ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

find_id = []

for ban_id in banned_id: # ban id
    temp_store = []
    for u_id in user_id:
        
        if len(ban_id) != len(u_id):
            continue
        correct_flag = 1
    
        for k in range(len(ban_id)):
            if ban_id[k] == "*":
                continue
            if ban_id[k] != u_id[k]:
                correct_flag = 0
                break
        
        if correct_flag:
            temp_store.append(u_id)
    find_id.append(temp_store)
print(find_id)    

# bfc

from collections import deque
my_que = deque([[[],[],0]]) # use_user_list ,find_list, find_index
use_user_list = []
find_list = []
answer = []
my_que_input_list = []
while True:
    if len(my_que) == 0:
        break
    temp_use_user_list , temp_find_list ,now_index = my_que.popleft()
    
    if now_index == len(banned_id):
        temp_use_user_list.sort()
        answer.append(temp_use_user_list)
        continue
    
    for i in find_id[now_index]:
        if i not in temp_use_user_list:
            temp1 = temp_use_user_list.copy()
            temp2 = temp_find_list.copy()
            
            temp1.append(i)
            temp2.append(i)
            temp1.sort()
            temp2.sort()
            if temp1 not in my_que_input_list:
                my_que.append([temp1, temp2,now_index+1])
                my_que_input_list.append(temp1)
    

print(answer)

count = 0
for i in range(len(answer) -1): #기준 
    for j in range(i+1,len(answer)): # 비교
        
        if answer[i] == answer[j]:
            print(answer[i] , answer[j])
            print(answer[i] == answer[j])
            print("=======================")
            count += 1
            
            
print(len(answer) - count)