queue1 = [ 3, 3, 3, 3]
queue2 = [3, 3, 21, 3 ]

from collections import deque

q1 = deque(queue1)
q2 = deque(queue2)

q1_sum = sum(q1)
q2_sum = sum(q2)

total_min = (sum(queue1) + sum(queue2))
count = 0

if total_min % 2 != 0:
    answer = -1
else:
    total_min /= 2
    print("total_min",total_min)
    i = 0
    while True:
        if i> (len(queue1) *3):
            answer = -1
            break
        
        print(q1)
        print("q1_min",q1_sum)
        print(q2)
        print("q2_min",q2_sum)
        if q1_sum == total_min and q2_sum == total_min:
            answer = count
            break
        elif q1_sum > q2_sum:
            temp_pop = q1.popleft() 
            q1_sum -= temp_pop
            q2_sum += temp_pop
            q2.append(temp_pop)
            count +=1
        
        elif q2_sum > q1_sum:
            temp_pop = q2.popleft() 
            q2_sum -= temp_pop
            q1_sum += temp_pop
            q1.append(temp_pop)
            count +=1
        i +=1
    print("======================")
    
print(answer)