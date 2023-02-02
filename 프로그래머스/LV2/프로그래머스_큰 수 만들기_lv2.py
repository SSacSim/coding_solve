number = "1924"
k = 2

store_len = k + 1
# deque에 넣어 max를 찾는다. 
from collections import deque
my_q = deque([])

flag = 0
answer = ""
for index, i in enumerate(list(number)):
    
    while True:
        if len(my_q) == 0:
            my_q.append(int(i))
            break
        pop_number = my_q.pop()
        insert_number = int(i)
        
        print("popnumber",pop_number)
        print("insert_number",insert_number)
        if insert_number > pop_number:
            continue
            
        else:
            my_q.append(pop_number)
            my_q.append(insert_number)
            break
    
        print("afret q ",my_q)
    if index >= store_len - 1:
        answer += str(my_q.popleft())
    print("answer",answer)
        
    
    print("===========")

print(answer)