from collections import deque
N = int(input())
visit = []

my_q = deque([])

my_q.append( [N ,[N]] )

while my_q:

    now_num, length = my_q.popleft()
    
    if now_num == 1:
        print(len(length) - 1)
        print( *length)
        break
    
    if now_num % 3 == 0:
        if (now_num // 3) not in visit:
            visit.append(now_num // 3)
            my_q.append( [now_num//3 , length + [now_num // 3]] )
    if now_num % 2 == 0:
        if (now_num // 2) not in visit:
            visit.append(now_num // 2)
        my_q.append( [now_num//2 , length + [now_num // 2]] )
    if (now_num - 1 ) not in visit:
        visit.append(now_num -1)
        my_q.append( [now_num - 1 , length + [now_num - 1]] )